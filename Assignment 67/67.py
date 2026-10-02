import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Task 1: Create dataset [Age, Monthly Charges, Tenure, Complaints, Support Calls]
X = np.array([
    [25, 500, 12, 1, 2], [30, 700, 24, 0, 1], [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10], [28, 600, 18, 1, 1], [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9], [52, 1600, 3, 8, 12], [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])
y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# Task 2: Clean dataset (check missing values and duplicates)
print("Missing values:", np.isnan(X).sum())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Task 3: StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Task 4: Train FNN model
model = Sequential([
    Input(shape=(5,)),
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, verbose=0)

# Task 5: Evaluate accuracy
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy =", acc)

# Test input
new_customer = scaler.transform([[46, 1450, 5, 6, 9]])
pred = model.predict(new_customer, verbose=0)[0][0]
if pred >= 0.5:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")