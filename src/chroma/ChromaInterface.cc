#include "ChromaInterface.hh"

#include "G4Track.hh"
#include "G4VProcess.hh"
#include "G4Step.hh"
#include "G4VParticleChange.hh"
#include "G4StepPoint.hh"

#include "GLG4VEventAction.hh"
#include "GLG4HitPhoton.hh"

#include <RAT/DB.hh>
#include <RAT/Log.hh>



namespace RAT {

  ChromaInterface::ChromaInterface() {
    GOOGLE_PROTOBUF_VERIFY_VERSION; // checks protobuf version
    ClearData();
  }


  ChromaInterface::~ChromaInterface() {
  }

  void ChromaInterface::initializeServerConnection() {
    // Load the Chroma Table
    DB* db = DB::Get();
    DBLinkPtr lChroma = db->GetLink("CHROMA");

    fStrQueueAdress = lChroma->GetS("QueueManagerAddress");
    try {
      info << "Chroma/RAT Queue manager address is " << fStrQueueAddress << newline;
    }
    catch ( DBNotFoundError& e) {
      Log::Die( "Chroma interface initialized without specifying Chroma/RAT Queue manager address." );
    }

    // Here load appropriate socket
    context =  new zmq::context_t(1);//flag=# of i/o threads, apparently
    client = S_Client_Socket (*context);
    SetIdentity();
    JoinQueue();
    // Gather required geometry data
    
    // Talk to Server/Handshake/Send out detector data
    SendDetectorConfigData();
  }

  void ChromaInterface::closeServerConnection() {
    delete client; // close socket
    delete context;
  }

  void ChromaInterface::readStoreKillCherenkovPhotons( std::vector< G4Track* >* secondaries ) {
  

    for (  std::vector< G4Track* >::const_iterator it=secondaries->begin(); it!=secondaries->end(); it++ ) {

      if ( (*it)->GetParticleDefinition()->GetParticleName()=="opticalphoton" && (*it)->GetCreatorProcess()->GetProcessName()=="cerenkov" ) {
	std::cout << "  " << (*it)->GetParticleDefinition()->GetParticleName() << " " << (*it)->GetCreatorProcess()->GetProcessName() << std::endl;
	// create new data
	ratchroma::CherenkovPhoton* cerenkov = message.add_cherekovdata();
	cerenkov->set_x( (*it)->GetVertexPosition().x() );
	cerenkov->set_y( (*it)->GetVertexPosition().y() );
	cerenkov->set_z( (*it)->GetVertexPosition().z() );
	cerenkov->set_t( (*it)->GetGlobalTime() );
	cerenkov->set_dx( (*it)->GetVertexMomentumDirection().x() );
	cerenkov->set_dy( (*it)->GetVertexMomentumDirection().y() );
	cerenkov->set_dz( (*it)->GetVertexMomentumDirection().z() );
	double ke = (*it)->GetVertexKineticEnergy(); // MeV
	double wavelength = ke; // MeV -> nanometers
	cerenkov->set_wavelength( wavelength );
	cerenkov->set_px( (*it)->GetPolarization().x() );
	(*it)->SetTrackStatus( fStopAndKill ); // we take this over now!
      }    
    }
  }

  void ChromaInterface::readStoreKillScintillationPhotons( const G4Step* aStep, G4VParticleChange* scint_photons ) {

    G4int iSecondary= scint_photons->GetNumberOfSecondaries();
    if ( iSecondary==0 )
      return;

    ratchroma::ScintStep* scintinfo = message.add_stepdata();
    G4StepPoint* prestep = aStep->GetPreStepPoint();
    G4StepPoint* poststep = aStep->GetPostStepPoint();

    scintinfo->set_nphotons( (int)iSecondary );
    scintinfo->set_step_start_x( prestep->GetPosition().x() );
    scintinfo->set_step_start_y( prestep->GetPosition().y() );
    scintinfo->set_step_start_z( prestep->GetPosition().z() );
    scintinfo->set_step_end_x( poststep->GetPosition().x() );
    scintinfo->set_step_end_y( poststep->GetPosition().y() );
    scintinfo->set_step_end_z( poststep->GetPosition().z() );
    scintinfo->set_material( prestep->GetMaterial()->GetName() );
    scint_photons->Clear();
  }

  void ChromaInterface::ClearData() {
    message.Clear();
    //fPhotonData.Clear();
  }

  void ChromaInterface::JoinQueue() {
    zhelpers::s_send (*client, "RDY");
  }
  //must initialize client before setting its identity
  void ChromaInterface::SetIdentity() {
    //uses zhelpers member function to set a random identity.
    //(this method is thread-safe)
    ClientIdentity = zhelpers::s_set_id(*client);
  }
  void ChromaInterface::SendPhotonData() {
    // Send data
    //basic implementation, probably want to handshake or do
    //some check first.
    zhelpers::s_recv(*client); //signal
    std::string str_msg;
    message.SerializeToString(&str_msg);
    zhelpers::s_send (*client, str_msg);
  }

  void ChromaInterface::ReceivePhotonData() {
    //do some check/confirmation first
    const std::string msg = zhelpers::s_recv (*client);
    fPhotonData.ParseFromString(msg);
    std::cout << "Got the photon data." << "\n";
  }

  void ChromaInterface::SendDetectorConfigData() {
    // Send geometry information.
    // Includes mesh representation of detector (or activation of cache).  
    // Also, geometry info has to sync. optical detector indexes between Chroma and RAT

    //just sending # of pmts for now
    zhelpers::s_recv(*client);
    zhelpers::s_send(*client,"5");
  }

  void ChromaInterface::MakePhotonHitData() {
    //hit_photon->SetPMTID((int)iopdet);
    for (int i = 0; i < fPhotonData.photon_size(); i++) 
      {
	GLG4HitPhoton* hit_photon = new GLG4HitPhoton();
	hit_photon->SetPMTID(fPhotonData.photon(i).pmtid());
	hit_photon->SetTime(fPhotonData.photon(i).time());
	hit_photon->SetKineticEnergy(fPhotonData.photon(i).kineticenergy());
	hit_photon->SetPosition((fPhotonData.photon(i).posx()),
				(fPhotonData.photon(i).posy()),
				(fPhotonData.photon(i).posz()));
	hit_photon->SetMomentum((fPhotonData.photon(i).momx()),
				(fPhotonData.photon(i).momy()),
				(fPhotonData.photon(i).momz()));
	hit_photon->SetPolarization((fPhotonData.photon(i).polx()),
				    (fPhotonData.photon(i).poly()),
				    (fPhotonData.photon(i).polz()));
	hit_photon->SetCount(fPhotonData.photon(i).count());
	hit_photon->SetTrackID(fPhotonData.photon(i).trackid());
	hit_photon->SetOriginFlag(fPhotonData.photon(i).origin());
	GLG4VEventAction::GetTheHitPMTCollection()->DetectPhoton(hit_photon);
      }
  }

  //returns a REQ client
  zmq::socket_t* ChromaInterface::S_Client_Socket (zmq::context_t & context)
  {
    zmq::socket_t * client = new zmq::socket_t (context, ZMQ_REQ);
    client->connect ("tcp://localhost:5554");
    //can write this more generally (to connect to another
    //port) if we need to
    return client;
  }
}// end of namespace RAT


