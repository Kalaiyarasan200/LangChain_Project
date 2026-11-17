import os
import sqlite3
from pathlib import Path

# Resolve path relative to this script so it works from any working directory
BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "SalesDB"
DB_NAME = str(DB_DIR / "sales.db")

def init_db():
    # Ensure the parent directory exists
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the sales table (drop it first so the script can be re-run)
    cursor.execute("DROP TABLE IF EXISTS sales")
    cursor.execute("""
        CREATE TABLE sales (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            product     TEXT NOT NULL,
            quantity    INTEGER NOT NULL,
            price       REAL NOT NULL,
            sale_date   TEXT NOT NULL
        )
    """)

    # Sample data
    sample_sales = [
        ("Laptop",     2, 999.99, "2024-01-05"),
        ("Mouse",     10,  19.99, "2024-01-06"),
        ("Keyboard",   5,  49.50, "2024-01-07"),
        ("Monitor",    3, 199.00, "2024-02-10"),
        ("Laptop",     1, 999.99, "2024-02-15"),
        ("Headphones", 4,  79.95, "2024-03-01"),
    ]

    cursor.executemany(
        "INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)",
        sample_sales
    )

    conn.commit()
    print(f"Database '{DB_NAME}' initialized successfully with {len(sample_sales)} records.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
