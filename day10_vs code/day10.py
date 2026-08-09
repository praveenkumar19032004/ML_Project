import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Manual Dataset
data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Attendance': [60,65,70,72,75,80,85,88,90,95],
    'Previous_Score': [50,55,60,62,68,72,78,82,88,92],
    'Final_Score': [52,58,63,67,72,77,83,87,91,96]
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Hours_Studied', 'Attendance', 'Previous_Score']]
y = df['Final_Score']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R² Score:", round(r2, 2))
