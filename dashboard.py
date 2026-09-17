import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed_customer_data.csv")

# 1. Customer Churn Distribution
plt.figure(figsize=(7, 5))
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.close()

# 2. Income vs Total Spending
plt.figure(figsize=(8, 5))
plt.scatter(df["Annual_Income"], df["Total_Spending"])
plt.title("Annual Income vs Total Spending")
plt.xlabel("Annual Income")
plt.ylabel("Total Spending")
plt.tight_layout()
plt.savefig("income_vs_spending.png")
plt.close()

# 3. Customer Satisfaction
plt.figure(figsize=(8, 5))
df["Customer_Satisfaction"].plot(kind="hist", bins=10)
plt.title("Customer Satisfaction Distribution")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_satisfaction.png")
plt.close()

# 4. Website Visits vs Spending
plt.figure(figsize=(8, 5))
plt.scatter(df["Website_Visits"], df["Total_Spending"])
plt.title("Website Visits vs Total Spending")
plt.xlabel("Website Visits")
plt.ylabel("Total Spending")
plt.tight_layout()
plt.savefig("visits_vs_spending.png")
plt.close()

print("Dashboard visualizations created successfully!")
print("4 charts generated.")