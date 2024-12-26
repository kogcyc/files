# ANSI escape codes for ANSI
ANSI = {
    "r": "\033[91m",
    "y": "\033[93m",
    "c": "\033[96m",
    "g": "\033[92m",
    "m": "\033[95m",
    "r": "\033[0m",  # Reset to default color
}

# Print text in different ANSI
print(f"{ANSI['r']}This is bright red text!{ANSI['r']}")
print(f"{ANSI['y']}This is yellow text!{ANSI['r']}")
print(f"{ANSI['c']}This is cyan text!{ANSI['r']}")
print(f"{ANSI['g']}This is green text!{ANSI['r']}")
print(f"{ANSI['m']}This is magenta text!{ANSI['r']}")
