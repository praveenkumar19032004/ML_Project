import pandas as pd
from sklearn.linear_model import LinearRegression

# Student dataset
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [30, 38, 45, 52, 60, 68, 75, 85, 95]
})

# Train the model
X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

# New data for prediction
new_hours = pd.DataFrame({"Hours": [2, 4.5, 6.5, 8]})

# Predict marks
predicted_marks = model.predict(new_hours)

# Print results
result = pd.DataFrame({
    "Study Hours": new_hours["Hours"],
    "Predicted Marks": predicted_marks.round(2)
})

print(result)
