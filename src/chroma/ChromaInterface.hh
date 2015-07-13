#ifndef __CHROMA_INTERFACE__
#define __CHROMA_INTERFACE__

#include <vector>
#include <string>
#include <fstream>

#if defined(_HAS_ZMQ) && defined(_HAS_PROTOBUF)
#define _HAS_CHROMA_INTERFACE
#endif

#ifdef _HAS_PROTOBUF
#include "ratchromadata.pb.h"
#include "photonHit.pb.h"
#endif

#ifdef _HAS_ZMQ
#include "zhelpers.hpp"
#endif


class G4Track;
class G4VParticleChange;
class G4Step;

namespace RAT {

class ChromaInterface {

public:

  ChromaInterface();
  ~ChromaInterface();

  bool isActive();

  void initializeServerConnection();
  void closeServerConnection();
  void readStoreKillCherenkovPhotons( std::vector< G4Track* >* secondaries );
  void readStoreKillScintillationPhotons( const G4Step* astep, G4VParticleChange* scint_photons );
  void ClearData();
  void SendPhotonData();
  void ReceivePhotonData();
  void SendDetectorConfigData();
  void MakePhotonHitData();
#ifdef _HAS_ZMQ
  void JoinQueue();  
  void SetIdentity();  
  zmq::socket_t * S_Client_Socket (zmq::context_t & context);
#endif
#ifndef _HAS_CHROMA_INTERFACE
  void NoSupportWarning();
#endif

protected:
  #ifdef _HAS_ZMQ
  zmq::socket_t *client;
  zmq::context_t *context;
  #endif
  #ifdef _HAS_PROTOBUF
  ratchroma::ChromaData message; // data we send to Chroma
  hitPhotons::PhotonHits fPhotonData;
  #endif
  bool fActive;
  std::string fStrQueueAddress;
  std::string ClientIdentity;
};

}// end of RAT namespace

#endif
