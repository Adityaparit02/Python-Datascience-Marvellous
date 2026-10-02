import math

# Inputs, weights and bias
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# Task 1: Weighted sum
z = (x1 * w1) + (x2 * w2) + bias
print("Weighted sum (z) =", z)

# Task 2: Sigmoid activation
output = 1 / (1 + math.exp(-z))

# Task 3: Final output
print("Final output =", round(output, 4))

# Task 4: Close to 0 or 1?
if output >= 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")