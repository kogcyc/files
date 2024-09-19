```openscad

// Toggle between 2D and 3D output
is_2D = true;  // Set this to 'false' for 3D output

// Function to calculate the circumradius of a regular polygon
// Based on the number of teeth and the pitch (default pitch = 12.7mm)
function rivit_radius_polygon(teeth, pitch = 12.7) =
    pitch / (2 * sin(180 / teeth));

// Function to generate a range of angles for each tooth
// 'divisions' represents the number of teeth
function angle_range(divisions) = [0 : 360 / divisions : 360];

// Variables for the sprocket configuration
teeth = 11;                   // Number of teeth
kolor = [0.5, 0.5, 0.5];      // Grey color
angles = angle_range(teeth);   // Array of angles for each tooth
circumradius = rivit_radius_polygon(teeth);  // Calculate circumradius
roller = 3.96875;             // Radius of the roller
tooth_height = -1;            // Tooth height adjustment
tooth_angle = 30;             // Angle for the tooth's triangular shape

// Function to apply conditional extrusion based on is_2D flag
// If extrusion is enabled, it extrudes the shape to the specified height
// The 'center' parameter determines if the extrusion is centered or not
module conditional_extrude(height, enable, center) {
    if (enable)
        linear_extrude(height = height, center = center)
            children();
    else
        children();  // No extrusion, just render the 2D shapes
}

// Main block that generates the sprocket shape
// It uses a difference operation to subtract shapes
color(kolor)  // Set the color for the sprocket
difference() {
    // Outer sprocket circle (with or without extrusion based on is_2D)
    conditional_extrude(2, !is_2D, true) {
        circle(r = circumradius + tooth_height, $fn = 100);  // Outer circle
    }

    // Loop over all angles to position and generate each tooth
    for (angle = angles) {
        rotate(angle) {
            translate([circumradius, 0, 0]) {
                union() {
                    // Create two mirrored tooth shapes and a circle at the roller position
                    conditional_extrude(3, !is_2D, true) {
                        rotate([0, 0, tooth_angle])
                            polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);
                        
                        rotate([0, 0, -tooth_angle])
                            polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);
                        
                        // Circle at the roller position
                        circle(r = roller, $fn = 100);
                    }
                }
            }
        }
    }

    // Inner circle (with or without extrusion based on is_2D)
    conditional_extrude(3, !is_2D, true) {
        circle(r = circumradius - 12, $fn = 100);  // Inner circle
    }
}

```
