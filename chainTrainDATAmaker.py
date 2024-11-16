import math
from random import randint

def chain_length(chainring, sprocket, C):
    """
    Calculate the length of a chain connecting two pulleys.
    
    Parameters:
        chainring (float): Circumference of the larger pulley in units.
        sprocket (float): Circumference of the smaller pulley in units.
        C (float): Distance between the centers of the two pulleys in units.
    
    Returns:
        float: Total length of the chain in units.
    """
    # Calculate radii from circumferences
    R1 = (chainring*12.7) / (2 * math.pi)
    R2 = (sprocket*12.7) / (2 * math.pi)
    
    # Ensure the configuration is valid
    if C <= abs(R1 - R2):
        raise ValueError("The center distance is too small to connect the pulleys.")
    
    # Calculate tangency angle
    theta = math.acos((R1 - R2) / C)
    
    # Calculate arc lengths
    arc_length1 = R1 * (2 * theta)
    arc_length2 = R2 * (2 * theta)
    
    # Calculate straight chain length
    straight_length = 2 * math.sqrt(C**2 - (R1 - R2)**2)
    
    # Total chain length
    total_length = arc_length1 + arc_length2 + straight_length
    return total_length / 12.7

csv = ''
for t in range(40000):
  c = randint(24,53)
  s = randint(11,30)
  cs = randint(300,500)
  chain = chain_length(c,s,cs)
  outstr = f'{c},{s},{cs},{chain}\n'
  if c > s:
    csv = csv + outstr

with open('chainTrain.csv','w') as outfil:
  outfil.write(csv)

print("model data stored to chainTrain.scv successfully!")
print("ready to run chainTrain.py")