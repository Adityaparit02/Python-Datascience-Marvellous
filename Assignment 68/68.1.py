image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

k = 3
out_size = len(image) - k + 1          # 5 - 3 + 1 = 3
feature_map = [[0] * out_size for _ in range(out_size)]

for i in range(out_size):
    for j in range(out_size):
        # extract the 3x3 region
        region = [row[j:j + k] for row in image[i:i + k]]

        total = 0
        terms = []
        for m in range(k):
            for n in range(k):
                total += region[m][n] * kernel[m][n]
                terms.append(f"{region[m][n]}*{kernel[m][n]}")

        feature_map[i][j] = total

        print(f"Region at ({i},{j}):")
        for row in region:
            print(*row)
        print("Calculation:", " + ".join(terms))
        print("Output =", total, "\n")

print("Feature Map:")
for row in feature_map:
    print(row)