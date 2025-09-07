#  BREAK Example: Stop loop when a condition is met
print("🔹 BREAK Example: Stop printing when number is divisible by 4")
i = 1
while i <= 10:
    if i % 4 == 0:
        print(f"Stopping at {i} (divisible by 4)")
        break
    print(i)
    i += 1

#  CONTINUE Example: Skip specific values
print("\n🔹 CONTINUE Example: Skip multiples of 3")
i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

#  PASS Example: Placeholder for future logic
print("\n🔹 PASS Example: Placeholder for even numbers")
i = 0
while i <= 10:
    if i % 2 == 0:
        pass  # You can add logic here later
    else:
        print(f"Odd number: {i}")
    i += 1