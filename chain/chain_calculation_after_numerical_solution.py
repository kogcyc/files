from math import pi, sqrt, asin, sin

P = 12.7            # chain pitch (mm)
Ts = 15             # small sprocket teeth
Tl = 45             # large sprocket teeth
C_guess = 340.0     # starting center distance (mm)

# --- Pitch radii ---
Rl = P / (2 * sin(pi / Tl))
Rs = P / (2 * sin(pi / Ts))


# ----------------------------------------------------------
# Continuous chain length function
# ----------------------------------------------------------

def chain_links(C):
    alpha = asin((Rl - Rs) / C)

    L = (
        2 * sqrt(C*C - (Rl - Rs)*(Rl - Rs))
        + Rs * (pi + 2*alpha)
        + Rl * (pi - 2*alpha)
    )

    return L / P


# ----------------------------------------------------------
# 1) Compute continuous N at the guess
# ----------------------------------------------------------

N_cont = chain_links(C_guess)

# Force to nearest EVEN integer
N_target = int(round(N_cont / 2)) * 2


# ----------------------------------------------------------
# 2) Solve for C such that N(C) = N_target
#    using BISECTION METHOD
# ----------------------------------------------------------

# Choose a bracket where solution must lie
C_low  = abs(Rl - Rs) + 1.0
C_high = C_guess * 2.0

for _ in range(60):      # ~ double precision accuracy
    C_mid = 0.5 * (C_low + C_high)

    if chain_links(C_mid) < N_target:
        C_low = C_mid
    else:
        C_high = C_mid

C_fit = 0.5 * (C_low + C_high)


# ----------------------------------------------------------
# Output
# ----------------------------------------------------------

alpha = asin((Rl - Rs) / C_fit)

L = (
    2 * sqrt(C_fit*C_fit - (Rl - Rs)*(Rl - Rs))
    + Rs * (pi + 2*alpha)
    + Rl * (pi - 2*alpha)
)

print("Small teeth =", Ts)
print("Large teeth =", Tl)
print("Pitch P =", P, "mm")
print()
print("Fitted center distance C =", C_fit, "mm")
print("Even link count N =", N_target)
print("Resulting chain length L =", L, "mm")