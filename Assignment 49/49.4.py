import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance

# Two points (each with 2 features, e.g. age and salary)
point1 = np.array([25, 20000])
point2 = np.array([35, 80000])

# ---- Distance BEFORE scaling ----
dist_before = distance.euclidean(point1, point2)

# ---- Apply scaling (fit on both points together) ----
data = np.array([point1, point2])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

point1_scaled = scaled_data[0]
point2_scaled = scaled_data[1]

# ---- Distance AFTER scaling ----
dist_after = distance.euclidean(point1_scaled, point2_scaled)

print("Point 1:", point1, " Point 2:", point2)
print("Euclidean Distance BEFORE scaling:", dist_before)
print("Euclidean Distance AFTER scaling:", dist_after)