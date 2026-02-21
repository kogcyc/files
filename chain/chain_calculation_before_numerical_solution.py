from math import pi, sqrt, asin, sin

P = 12.7        # chain pitch (mm)
C = 340.0       # center distance (mm)

# Pitch radii from tooth counts
Rl = P / (2 * sin(pi / 45))
Rs = P / (2 * sin(pi / 15))

# Obliquity angle
alpha = asin((Rl - Rs) / C)

# Total chain path length (continuous model)
L = (
    2 * sqrt(C*C - (Rl - Rs)*(Rl - Rs))
    + Rs * (pi + 2*alpha)
    + Rl * (pi - 2*alpha)
)

# Equivalent number of links (not yet forced to integer)
N = L / P

print("Rl =", Rl)
print("Rs =", Rs)
print("alpha (deg) =", alpha * 180/pi)
print("Chain length L =", L, "mm")
print("Equivalent links N =", N)