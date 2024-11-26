
include </home/matt/Desktop/weld/weldbead.scad>;

difference() {
rotate([0,17,0])
cylinder(r=18, h=50, center=false, $fn=80);
rotate([0,17,0])
cylinder(r=17, h=51, center=false, $fn=80);
    
rotate([0,90,0])
cylinder(r=19, h=102, center=true, $fn=80);    
}

difference() {   
rotate([0,90,0])
cylinder(r=20, h=100, center=true, $fn=80);
rotate([0,90,0])
cylinder(r=19, h=102, center=true, $fn=80);
    
rotate([0,17,0])
cylinder(r=17, h=51, center=false, $fn=80);    
}