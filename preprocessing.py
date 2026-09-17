import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_customer_data.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Feature engineering
df["Total_Spending"] = (
    df["Total_Purchases"] * df["Average_Order_Value"]
)

df["Income_Per_Purchase"] = (
    df["Annual_Income"] / df["Total_Purchases"]
)

# Save processed dataset
df.to_csv("processed_customer_data.csv", index=False)

print("\nProcessed Shape:", df.shape)
print("Preprocessing completed successfully!")
print("Processed dataset saved successfully!")