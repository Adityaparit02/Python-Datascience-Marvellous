matrix = [
    [6, 4],
    [8, 6]
]

# Step 1: Flatten 2D -> 1D
flatten_output = [v for row in matrix for v in row]
print("Flatten Output:", flatten_output)

# Step 2: Fully connected layer (2 neurons, sample weights and bias)
weights = [
    [0.1, 0.2, 0.3, 0.4],   # neuron 1
    [0.5, 0.6, 0.7, 0.8]    # neuron 2
]
bias = [1, 2]

# Step 3: Manual calculation
output = []
for n in range(len(weights)):
    total = 0
    terms = []
    for i in range(len(flatten_output)):
        total += flatten_output[i] * weights[n][i]
        terms.append(f"{flatten_output[i]}*{weights[n][i]}")
    total += bias[n]
    output.append(round(total, 2))
    print(f"Neuron {n+1}: " + " + ".join(terms) + f" + {bias[n]} = {round(total, 2)}")

print("Final Output:", output)