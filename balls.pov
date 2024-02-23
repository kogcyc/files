camera {
  location <400, 400, -10000>
  look_at <400, 400, 0>
  angle 2
}

light_source {
  <4000 ,6000, -16500>
  color rgb <1, 1, 1> * 1.4
}

//background { color rgb <10/20, 10/20, 10/20> }

#declare MaxVal = 100;

#declare AllSpheres = union { // Union of all spheres
  #for (ix, 0, MaxVal - 1)
    #for (iy, 0, MaxVal - 1)
      sphere { <ix * 24, iy * 24, 0>, 4 pigment {rgb <06/20, 12/20, 17/20>} translate <0, 0, 0> }
    #end
  #end
}

difference {
  box { <0, 0, -1>, <1111,1111,15> pigment {rgb <07/20, 12/20, 18/20>}}
  AllSpheres // Subtracting the union of spheres from other objects
}

