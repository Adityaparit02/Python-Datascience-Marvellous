# Task 1: Input, weight, bias, target and learning rate
x = 2
w = 0.5
b = 0.1
target = 1.0
lr = 0.1

# Task 2: Prediction
prediction = (x * w) + b

# Task 3: Error (loss = 0.5 * error^2)
error = prediction - target

# Task 4: Gradient descent update
# dLoss/dw = error * x ,  dLoss/db = error
new_w = w - lr * (error * x)
new_b = b - lr * error

# Task 5: Display old and updated weight
print("Prediction =", prediction)
print("Error =", error)
print("Old weight =", w)
print("Updated weight =", round(new_w, 4))
print("Old bias =", b)
print("Updated bias =", round(new_b, 4))