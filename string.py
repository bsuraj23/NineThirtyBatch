
n = 5  # Number of rows for the top half
diamond = ""

# Top half
for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    diamond += spaces + stars + "\n"

# Bottom half
for i in range(n - 2, -1, -1):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    diamond += spaces + stars + "\n"

