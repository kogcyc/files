# ANSI escape codes for colors
colors = {
    "bright_red": "\033[91m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "magenta": "\033[95m",
    "reset": "\033[0m",  # Reset to default color
}

# Print text in different colors
print(f"{colors['bright_red']}This is bright red text!{colors['reset']}")
print(f"{colors['yellow']}This is yellow text!{colors['reset']}")
print(f"{colors['cyan']}This is cyan text!{colors['reset']}")
print(f"{colors['green']}This is green text!{colors['reset']}")
print(f"{colors['magenta']}This is magenta text!{colors['reset']}")
