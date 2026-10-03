feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

def show(title, matrix):
    print(title)
    for row in matrix:
        print(row)
    print()

# Step 1: input
show("Input Feature Map:", feature_map)

# Step 2: ReLU
relu_output = [[max(0, v) for v in row] for row in feature_map]
show("After ReLU:", relu_output)

# Step 3: 2x2 Max Pooling (stride 2)
size, stride = 2, 2
pooled = []
for i in range(0, len(relu_output) - size + 1, stride):
    pooled_row = []
    for j in range(0, len(relu_output[0]) - size + 1, stride):
        window = [row[j:j + size] for row in relu_output[i:i + size]]
        pooled_row.append(max(max(r) for r in window))
    pooled.append(pooled_row)
show("After 2x2 Max Pooling:", pooled)