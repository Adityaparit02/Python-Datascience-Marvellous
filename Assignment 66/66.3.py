import math

# Task 3: Actual and predicted values
actual = [1, 0, 1, 1, 0]
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]
n = len(actual)

# Task 1: Mean Squared Error
mse = 0
for y, p in zip(actual, predicted):
    mse += (y - p) ** 2
mse = mse / n

# Task 2: Binary Cross Entropy
bce = 0
for y, p in zip(actual, predicted):
    bce += y * math.log(p) + (1 - y) * math.log(1 - p)
bce = -bce / n

# Task 4: Display loss
print("Mean Squared Error =", round(mse, 4))
print("Binary Cross Entropy =", round(bce, 4))