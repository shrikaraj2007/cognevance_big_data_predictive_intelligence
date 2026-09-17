import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "Customer_ID": range(1, n + 1),
    "Age": np.random.randint(18, 65, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Annual_Income": np.random.randint(20000, 150000, n),
    "Total_Purchases": np.random.randint(1, 50, n),
    "Average_Order_Value": np.round(np.random.uniform(20, 500, n), 2),
    "Website_Visits": np.random.randint(1, 30, n),
    "Customer_Satisfaction": np.round(np.random.uniform(1, 5, n), 1),
    "Previous_Returns": np.random.randint(0, 10, n)
}

df = pd.DataFrame(data)

# Create customer churn target
df["Churn"] = (
    (df["Website_Visits"] < 8) |
    (df["Customer_Satisfaction"] < 2.5) |
    (df["Previous_Returns"] > 6)
).astype(int)

df.to_csv("ecommerce_customer_data.csv", index=False)

print("Dataset created successfully!")
print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())