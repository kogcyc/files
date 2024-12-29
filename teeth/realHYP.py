import math

def origin_to_vertex(n, l=12.7):
    """
    Calculate the distance from the center of a regular polygon with n sides to one of its vertices.
    
    Args:
    - n (int): Number of sides of the polygon.
    - l (float): Length of each side of the polygon. Default is 12.7, representing the number of millimeters
                 in a link of a bicycle chain.
    
    Returns:
    - float: Distance from the center to one of the vertices.
    """
    if n < 3:
        return "A polygon must have at least 3 sides."
    if l <= 0:
        return "Length of each side must be positive."
    
    # Calculate the central angle of one of the sectors
    central_angle = 2 * math.pi / n
    
    # Calculate the distance using trigonometry
    distance = l / (2 * math.sin(math.pi / n))
    
    return distance

