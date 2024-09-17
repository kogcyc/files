// Function to calculate the circumradius of a regular polygon
function rivit_radius_polygon(teeth, pitch = 12.7) =
    pitch / (2 * sin(180 / teeth));

// Function to generate a range of angles
function angle_range(divisions) = [0 : 360 / divisions : 360];

// Toggle between 2D and 3D output
is_2D = true;  // Set this to false for 3D output
teeth = 39;
kolor = [0.7, 0.5, 0.5];  // Grey color
angles = angle_range(teeth);
circumradius = rivit_radius_polygon(teeth);
roller = 3.96875;

// Function to apply extrusion conditionally with dynamic centering
module conditional_extrude(height, enable, center) {
    if (enable)
        linear_extrude(height = height, center = center)
            children();
    else
        children();
}

sub_angle = 180 / teeth;
for (angle = angles) {
    rotate(angle + sub_angle) {
        translate([circumradius + 0.4, 0, 0]) {
            scale([1.99, 1.98, 1])
                circle(r = 1, $fn = 40);
        }
    }
}

// Main difference block with conditional extrusion
color(kolor)
difference() {
    conditional_extrude(2, !is_2D, true) {
        circle(r = circumradius + 1, $fn = teeth*2);
    }

    for (angle = angles) {
        rotate(angle) {
            translate([circumradius, 0, 0]) {
                union() {
                    conditional_extrude(3, !is_2D, true) {
                        rotate([0, 0, 20])
                            polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);
                        rotate([0, 0, -20])
                            polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);
                        circle(r = roller, $fn = 50);
                    }
                }
            }
        }
    }

    conditional_extrude(3, !is_2D, true) {
        circle(r = 49, $fn = 44);
    }
    
bcr = 116/2.0;
for (i = [0:2]) {
    rotate(i*120) {
        translate([bcr, 0, 0]) {
            scale([1, 1, 1])
                circle(r = 5, $fn = 20);
        }
    }
    
    
    for (i = [0:2]) {
    rotate(i*120+60) {
        translate([33, 0, 0]) {
            scale([6.5, 8, 1])
                circle(r = 5, $fn = 60);
        }
    }
}
}

    
}
