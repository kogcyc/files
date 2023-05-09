import math

def deflection_weight(OD=28.6, L=500, F=10, w=1.6, material='aluminum'):
    # Modulus of elasticity for steel, aluminum, and titanium in GPa
    E = {'steel': 210, 'aluminum': 70, 'titanium': 116}
    density = {'steel': 0.00785, 'aluminum': 0.00270, 'titanium': 0.00451}

    ID = OD - 2 * w

    aOD = math.pi * (OD / 2.0) ** 2
    aID = math.pi * (ID / 2.0) ** 2
    volume = (aOD - aID) * L
    print(f"Volume: {volume:.2f}")

    weight = volume * density[material]
    print(f"Weight: {weight:.2f} g")

    I = math.pi * (OD ** 4 - ID ** 4) / 64
    F_N = F * 9.81  # convert kg to N

    δ = (F_N * L ** 3) / (48 * E[material] * 1e3 * I)  # convert E to MPa
    return (δ, weight)


# Example usage
# δ, weight = deflection_weight(OD=28.6, L=500, F=10, w=1.6, material='aluminum')
# print(f"The deflection of the tube is {δ:.2f} mm")
# print(f"The weight of the tube is {weight:.2f} g")
