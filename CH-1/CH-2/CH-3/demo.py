import sqlite3
from pathlib import Path

# Resolve path relative to this script so it works from any directory
BASE_DIR = Path(__file__).resolve().parent
DB_NAME = str(BASE_DIR / "SalesDB" / "sales.db")

def fetch_all_sales():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, product, quantity, price, sale_date FROM sales")
    rows = cursor.fetchall()

    print("=== All Sales ===")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def fetch_sales_by_product(product_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parameterized query to safely filter by product
    cursor.execute(
        "SELECT id, product, quantity, price, sale_date FROM sales WHERE product = ?",
        (product_name,)
    )
    rows = cursor.fetchall()

    print(f"\n=== Sales for '{product_name}' ===")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def fetch_total_revenue_by_product():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT product, SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC
    """)
    rows = cursor.fetchall()

    print("\n=== Total Revenue by Product ===")
    for product, revenue in rows:
        print(f"{product}: ${revenue:,.2f}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_all_sales()
    fetch_sales_by_product("Laptop")
    fetch_total_revenue_by_product()