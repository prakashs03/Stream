import pandas as pd
import sqlite3

# Load your scraped CSV data
df = pd.read_csv("imdb_2024_full.csv")

# Optional: clean votes and duration if needed
df["Votes"] = df["Votes"].astype(str).str.replace(",", "").str.extract(r"(\d+)").fillna(0).astype(int)
df["Duration"] = df["Duration"].str.extract(r'(\d+)').fillna(0).astype(int)

# Connect to SQLite database (or create one)
conn = sqlite3.connect("imdb2024.db")

# Store the DataFrame in a table named 'movies'
df.to_sql("movies", conn, if_exists="replace", index=False)

print(" Data stored in 'imdb2024.db' in table 'movies'")

# Optional: show a sample SQL query
query = "SELECT Title, Genre, Rating FROM movies WHERE Rating > 7.0"
result = pd.read_sql(query, conn)
print("\n Sample High Rated Movies:\n", result.head())

# Close the connection
conn.close()
