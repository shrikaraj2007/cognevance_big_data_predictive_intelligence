import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load processed dataset
df = pd.read_csv("processed_customer_data.csv")

# Features
features = [
    "Age",
    "Annual_Income",
    "Total_Purchases",
    "Average_Order_Value",
    "Website_Visits",
    "Customer_Satisfaction",
    "Previous_Returns",
    "Total_Spending",
    "Income_Per_Purchase"
]

X = df[features]
y = df["Churn"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Customer Churn Prediction Model")
print("--------------------------------")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Predictive model completed successfully!")