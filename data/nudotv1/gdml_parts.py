import os,sys

part1 = """<?xml version="1.0" encoding="UTF-8"?>
<gdml xmlns:gdml="http://cern.ch/2001/Schemas/GDML"	
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="http://service-spi.web.cern.ch/service-spi/app/releases/GDML/schema/gdml.xsd" >

<define>
  <position name="photocathode_offset" unit="cm" x="0" y="0" z="0.5*11.0-0.5*0.1"/>
  <position name="origin" unit="cm" x="0" y="0" z="0"/>
  <rotation name="identity"/>
</define>

<materials>
  <element name="bromine" formula="Br" Z="35"> <atom value="79.904"/> </element>
  <element name="hydrogen" formula="H" Z="1">  <atom value="1.0079"/> </element>
  <element name="nitrogen" formula="N" Z="7">  <atom value="14.0067"/> </element>
  <element name="oxygen" formula="O" Z="8">  <atom value="15.999"/> </element>
  <element name="aluminum" formula="Al" Z="13"> <atom value="26.9815"/>  </element>
  <element name="silicon" formula="Si" Z="14"> <atom value="28.0855"/>  </element>
  <element name="carbon" formula="C" Z="6">  <atom value="12.0107"/>  </element>
  <element name="potassium" formula="K" Z="19"> <atom value="39.0983"/>  </element>
  <element name="chromium" formula="Cr" Z="24"> <atom value="51.9961"/>  </element>
  <element name="iron" formula="Fe" Z="26"> <atom value="55.8450"/>  </element>
  <element name="nickel" formula="Ni" Z="28"> <atom value="58.6934"/>  </element>
  <element name="calcium" formula="Ca" Z="20"> <atom value="40.078"/>   </element>
  <element name="magnesium" formula="Mg" Z="12"> <atom value="24.305"/>   </element>
  <element name="sodium" formula="Na" Z="11"> <atom value="22.99"/>    </element>
  <element name="titanium" formula="Ti" Z="22"> <atom value="47.867"/>   </element>
  <element name="argon" formula="Ar" Z="18"> <atom value="39.9480"/>  </element>
  <element name="boron" formula="B" Z="5"> <atom value="10.811"/> </element>
  
  <material Z="1" formula=" " name="Vacuum">
    <D value="1.e-25" unit="g/cm3"/>
    <atom value="1.0079"/>
  </material>

  <material name="stainless_steel" formula="stainless_steel">
    <D value="7.9300" unit="g/cm3"/>
    <fraction n="0.0010" ref="carbon"/>
    <fraction n="0.1792" ref="chromium"/>
    <fraction n="0.7298" ref="iron"/>
    <fraction n="0.0900" ref="nickel"/>
  </material>
  
  <material formula=" " name="air">
    <D value="0.001205" unit="g/cc"/>
    <fraction n="0.781154" ref="nitrogen"/>
    <fraction n="0.209476" ref="oxygen"/>
    <fraction n="0.00937" ref="argon"/>
  </material>
  
  <material formula=" " name="Dirt">
    <D value="1.7" unit="g/cc"/>
    <fraction n="0.438" ref="oxygen"/>
    <fraction n="0.257" ref="silicon"/>
    <fraction n="0.222" ref="sodium"/>
    <fraction n="0.049" ref="aluminum"/>
    <fraction n="0.019" ref="iron"/>
    <fraction n="0.015" ref="potassium"/>
  </material>
  
  <material formula=" " name="mineral_oil">
    <D value="0.77" unit="g/cc"/>
    <fraction n="0.8563" ref="carbon"/>
    <fraction n="0.1437" ref="hydrogen"/>
  </material>

  <material formula=" " name="pseudocumene">
    <D value="0.8758" unit="g/cc"/>
    <fraction n="0.8994" ref="carbon"/>
    <fraction n="0.1006" ref="hydrogen"/>
  </material>
  
  <material formula=" " name="ppo">
    <D value="1.06" unit="g/cc"/>
    <fraction n="0.8142" ref="carbon"/>
    <fraction n="0.0501" ref="hydrogen"/>
    <fraction n="0.0633" ref="nitrogen"/>
    <fraction n="0.0723" ref="oxygen"/>
  </material>
  
  <material formula=" " name="scintillator">
    <D value="0.78" unit="g/cc"/>
    <fraction n="0.996984" ref="mineral_oil"/>
    <fraction n="0.001919" ref="pseudocumene"/>
    <fraction n="0.001097" ref="ppo"/>
  </material>

  <material formula=" " name="chip_silicon">
    <D value="2.3" unit="g/cc"/>
    <fraction n="1.0" ref="silicon"/>
  </material>

  <material formula=" " name="borosilicate_glass">
    <D value="2.23" unit="g/cc"/>
    <fraction n="0.05238" ref="silicon"/>
    <fraction n="0.55873" ref="oxygen"/>
    <fraction n="0.38889" ref="boron"/>
  </material>

  <material formula=" " name="photocathode">
    <D value="5.0" unit="g/cc"/>
    <fraction n="1.0" ref="potassium"/>
  </material>

</materials>

<solids>

  <box name="world"
       lunit="m"
       x="10.0"
       y="10.0"
       z="10.0" />
  <box name="tankbox" lunit="cm" x="100" y="100" z="100"/>
  <box name="scintbox" lunit="cm" x="99" y="99" z="99"/>
  <tube name="pmt_bound" lunit="cm" aunit="deg" rmin="0" rmax="5.5" z="12.0" startphi="0" deltaphi="360.0"/>
  <tube name="pctube" lunit="cm" aunit="deg" rmin="0" rmax="4.7" z="0.1" startphi="0" deltaphi="360.0"/>
  <tube name="pmt_outertube" lunit="cm" aunit="deg" rmin="0" rmax="5.10" z="11.0" startphi="0" deltaphi="360.0"/>
  <tube name="pmt_shield" lunit="cm" aunit="deg" rmin="4.7" rmax="5.0" z="5.5" startphi="0" deltaphi="360.0"/>
  <subtraction name="pmt_glasstube">
    <first ref="pmt_outertube"/>
    <second ref="pctube"/>
    <positionref ref="photocathode_offset"/>
    <rotationref ref="identity"/>
  </subtraction> 

</solids>

<structure>
  <volume name="volPhotoCathode">
    <!-- <materialref ref="scintillator"/> -->
    <materialref ref="photocathode"/>
    <solidref ref="pctube"/>
  </volume>
  <volume name="volPMTShield">
    <materialref ref="aluminum"/>
    <solidref ref="pmt_shield"/>
  </volume>
  <volume name="volPMTGlassTube">
    <materialref ref="borosilicate_glass"/>
    <solidref ref="pmt_glasstube"/>
    <physvol>
      <volumeref ref="volPMTShield"/>
      <position name="posPMTShield" unit="cm" x="0" y="0" z="0.5*11.0-0.5*5.5"/>
    </physvol>
  </volume>
  <volume name="volPMTAssembly">
    <materialref ref="scintillator"/>
    <solidref ref="pmt_bound"/>
    <physvol>
      <volumeref ref="volPMTGlassTube"/>
      <positionref ref="origin"/>
    </physvol>
    <physvol>
      <volumeref ref="volPhotoCathode"/>
      <positionref ref="photocathode_offset"/>
    </physvol>
  </volume>
  
  <volume name="volScint">
    <materialref ref="scintillator"/>
    <solidref ref="scintbox"/>
    <!-- Add Photocathodes here -->
"""


part2 ="""    <!-- End of photocathodes -->
  </volume>

  <volume name="volTank">
    <materialref ref="stainless_steel"/>
    <solidref ref="tankbox"/>
    <physvol name="pvScint">
      <volumeref ref="volScint"/>
      <position name="posScint" x="0" y="0" z="0"/>
    </physvol>
  </volume>

  <volume name="volWorld">
    <materialref ref="air"/>
    <solidref ref="world"/>
    <physvol name="pvTank">
      <volumeref ref="volTank"/>
      <position name="posTank" unit="cm" x="0" y="0" z="0"/>
    </physvol>
  </volume>
</structure>

<setup name="Default" version="1.0">
  <world ref="volWorld" />
</setup>

</gdml>
"""
