

camera {  
  location  <1000,1000,1000>  
  look_at   <0,-0,0> 
  angle 5
}

light_source {
  <1200,1200,1200> 
  color rgb <1,1,1>
}

background { color rgb <0,0,0> }

cylinder {
  <0,0,0>
  <0,0,50> 
  18/1
  pigment { color rgb <0.7,0.6,0.5> }
  rotate <17,0,0>
}

cylinder {
  <0,50,0>
  <0,-50,0> 
  20/1
  pigment { color rgbf <0.7,0.6,0.5,0.0> }
}

union {
 #include "./weld.inc"
 rotate <0,0,270>
}