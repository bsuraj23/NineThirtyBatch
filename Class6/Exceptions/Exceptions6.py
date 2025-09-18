import math23

try:
    math23.sqrt(-1)
except ValueError:
    print("Math domain error")

try:
    import non_existing_module
except ModuleNotFoundError:
    print("Module not found")
