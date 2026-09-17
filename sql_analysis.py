import pandas as pd
import sqlite3

# Load processed dataset
df = pd.read_csv("processed_customer_data.csv")

# Create SQLite database
conn = sqlite3.connect("customer_analytics.db")

# Store data in SQL table
df.to_sql("customers", conn, if_exists="replace", index=False)

# SQL analysis
query = """
SELECT
    Gender,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Total_Spending), 2) AS Average_Spending,
    ROUND(AVG(Customer_Satisfaction), 2) AS Average_Satisfaction
FROM customers
GROUP BY Gender;
"""

result = pd.read_sql_query(query, conn)

print("Customer Analytics using SQL:")
print(result)

conn.close()

print("\nSQL analysis completed successfully!")