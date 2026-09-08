$fn=72;


// ================================
// DIFFERENCE
// ================================

module difference_part() {

    difference() {

        color("gray")
        scale([1,1.2,1])
        cylinder(160,50,50);

        color("gray")
        translate([0,0,-1])
        cylinder(162,46,46);

        color("gray")
        translate([0,0,120])
        cube([20,120,121],center=true);
    }
}


// ================================
// UNION / SEPARATOR
// ================================

module union_part() {

    union() {

        color("orange")
        translate([0,0,-1])
        cylinder(122,45,45);

        color("orange")
        translate([0,0,110])
        cube([20,130,101],center=true);
    }
}


// ================================
// ENABLE / DISABLE PARTS
// ================================

// Uncomment/comment these to turn parts on/off

difference_part();
union_part();
