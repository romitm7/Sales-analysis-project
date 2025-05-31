import pandas as pd
import mysql.connector

df = pd.read_csv("../data/sales_data.csv")
df['Date'] = pd.to_datetime(df['Date']).dt.date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Codex@1234?",
    database="sales_analysis"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales_data (Date, Sales_Rep, Product, Items_Sold, Sales_Amount, Profit)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row.values))

conn.commit()
cursor.close()
conn.close()

print("Data uploaded to MySQL successfully.")
