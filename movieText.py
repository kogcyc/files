# comment  """docstring""" 'single' "double" f"fstring {42}"
import math, os
from collections import defaultdict as dd

# numbers
x_int, x_float, x_hex = 123, 3.14, 0xFF

# keywords, builtins, identifiers
def foo(bar, baz=99):
    return bar + baz

class A:
    def method(self):
        print("hello", x_int, math.sqrt(x_float))

@staticmethod
def static_func(x):
    if x > 0:
        return x**2
    elif x == 0:
        return None
    else:
        return -x

y = [i for i in range(5) if i % 2 == 0]
g = (i**2 for i in y)
d = {"a":1, "b":2}

try:
    foo(1)
except Exception as e:
    pass
finally:
    print("done")
