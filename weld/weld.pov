
#include "colors.inc"

camera {  
  location  <1000,1000,000>  
  look_at   <0,0,0> 
  right -4/3
  angle 5
}

light_source {
  <1200,1300,-1400> 
  color White
}

background { color White }

cylinder {
  <0,0,0>
  <0,0,-100> 
  12.7
  pigment { color rgb <0.7,0.6,0.5> }
}

cylinder {
  <0,100,0>
  <0,-100,0> 
  14.3
  pigment { color rgbf <0.7,0.6,0.5,0.0> }
}

 #include "./weld.inc"