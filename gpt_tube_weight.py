import math

# Overall length of the tube
length = 600 # mm

# Outer diameter of the tube
outer_diameter = 34.9 # mm

# Butted wall thickness
butted_thickness = 0.9 # mm

# Thin-walled section thickness
thin_thickness = 0.6 # mm

# Length of the first butted section
butted1_length = 80 # mm

# Length of the second butted section
butted2_length = 180 # mm

# Length of the first transition section
transition1_length = 50 # mm

# Length of the second transition section
transition2_length = 50 # mm

# Density of steel
steel_density = 7850 # kg/m^3

# Calculate the inner diameter of the butted section
butted_inner_diameter = outer_diameter - 2 * butted_thickness

# Calculate the inner diameter of the thin-walled section
thin_inner_diameter = outer_diameter - 2 * thin_thickness

# Calculate the volume of the first butted end
butted1_volume = math.pi * (butted_inner_diameter/2)**2 * butted1_length

# Calculate the volume of the first transition section
transition1_volume = math.pi * ((outer_diameter + thin_inner_diameter)/4)**2 * transition1_length

# Calculate the volume of the thin-walled section between the butted ends
thin_volume = math.pi * (thin_inner_diameter/2)**2 * (length - butted1_length - transition1_length - butted2_length - transition2_length)

# Calculate the volume of the second butted end
butted2_volume = math.pi * (butted_inner_diameter/2)**2 * butted2_length

# Calculate the volume of the second transition section
transition2_volume = math.pi * ((outer_diameter + thin_inner_diameter)/4)**2 * transition2_length

# Calculate the total volume of the tube
total_volume = butted1_volume + transition1_volume + thin_volume + butted2_volume + transition2_volume

# Calculate the weight of the tube
weight = total_volume * steel_density / 10000000 # in grams

print("The weight of the butted steel tube is {:.2f} grams.".format(weight))
