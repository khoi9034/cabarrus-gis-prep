import pandas as pd
import sqlite3

# Define CSV path
file_path = r"C:\sql\data\KO_CocaCola_Stock_Prices_1980_2026.csv"

# 1️⃣ Load CSV into Pandas
df = pd.read_csv(file_path)

# 2️⃣ Connect to the EXACT database file location
conn = sqlite3.connect(r'C:\sql\coke_db.db')

# 3️⃣ Create/replace the table and push data into SQLite
df.to_sql('coke_prices', conn, if_exists='replace', index=False)

print("✅ Success! Data moved from CSV to SQL via Pandas.")

conn.close()