// User-defined parameters
teeth = 15;              // Number of teeth
extrusion_height = 3;    // Extrusion height for the features

// Function to calculate the circumradius of a regular polygon (sprocket-like structure)
// based on the number of teeth and the pitch distance between them.
function rivit_radius_polygon(teeth, pitch = 12.7) =
    pitch / (2 * sin(180 / teeth));  // Divides 360 degrees by the number of teeth to calculate angle and radius.

// Function to generate a range of angles by dividing 360 degrees based on the input number of divisions.
function angle_range(divisions) = [0 : 360 / divisions : 360];  // Returns a range of angles from 0 to 360.

angles = angle_range(teeth);  // Generates angles for the specified number of teeth.
echo(angles);  // Print the list of angles to the console.

circumradius = rivit_radius_polygon(teeth);  // Calculate circumradius based on the number of teeth and default pitch.
echo("Calculated circumradius: ", circumradius);  // Output the calculated circumradius to the console.

roller = 3.96875;  // Radius of the central "roller" circle that is repeated at each angle.

difference() {
    // Base circle representing the sprocket body, extruded to a height of 2mm.
    color([0.6, 0.5, 0.4])  // Light brown color for the base.
    linear_extrude(height = 2, center = true)
        circle(r = circumradius + 2, $fn = 100);  // The base circle with a radius slightly larger than the circumradius.

    // Loop to create features at each angle generated by angle_range (based on the number of teeth).
    for (angle = angles) {
        rotate(angle) {
            translate([circumradius, 0, 0]) {
                union() {
                    // First polygon extrusion, rotated 20 degrees clockwise.
                    color([0, 0, 0])  // Black color for the polygon.
                    linear_extrude(height = extrusion_height, center = true)
                        rotate([0, 0, 20])
                        polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);

                    // Second polygon extrusion, rotated 20 degrees counter-clockwise.
                    color([0, 0, 0])  // Black color for the polygon.
                    linear_extrude(height = extrusion_height, center = true)
                        rotate([0, 0, -20])
                        polygon(points = [[0, 0], [0, -roller], [20, -roller], [20, roller], [0, roller]]);

                    // Central circular extrusion representing a roller at each angle.
                    color([0, 0, 0])  // Black color for the circle.
                    linear_extrude(height = extrusion_height, center = true)
                        circle(r = roller, $fn = 100);
                }
            }
        }
    }

    // Inner circle that represents an inner boundary, extruded to the specified height.
    color([0, 0, 0])  // Black color for the inner circle.
    linear_extrude(height = extrusion_height, center = true)
        circle(r = circumradius - 12, $fn = 100);  // Smaller circle with reduced radius.
}
