smoothness = 111;

difference() {
    // Outer circle (base shape)
    difference() {
    circle(r = 30.319 + 1, $fn=smoothness);
    circle(r = 30.319 - 9, $fn=smoothness);
    }

    // Parameters for smaller holes and teeth
    radius = 25.4 * (5 / 16) / 2;
    tooth_angle = 20;

    // Loop to create smaller circles (holes) and teeth
    for (angle = [0 : 360 / 15 : 360]) {
        rotate([0, 0, angle]) {
            translate([30.319, 0, 0]) {

                // Create the smaller circle (hole)
                circle(r = radius, $fn=smoothness);

                // Create a tooth (rectangular) shape
                rotate([0, 0, tooth_angle]) {
                    square([5, radius]);
                }

                // Create mirrored tooth (rectangular) shape
                mirror([0, 1, 0]) {
                    rotate([0, 0, tooth_angle]) {
                        square([5, radius]);
                    }
                }
     
            }
        }
    }
}
