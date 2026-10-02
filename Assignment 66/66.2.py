import numpy as np
import matplotlib.pyplot as plt

# Task 1: Input values from -10 to 10
x = np.linspace(-10, 10, 200)

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Task 2: Plot all functions
plt.figure(figsize=(8, 5))
plt.plot(x, sigmoid(x), label="Sigmoid")
plt.plot(x, relu(x), label="ReLU")
plt.plot(x, tanh(x), label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()