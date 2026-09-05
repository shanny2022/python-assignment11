"""Task 1: query revenue per employee and plot it using Pandas."""
from contextlib import closing
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
DB_PATH = HERE.parent / "db/lesson.db"


def load_employee_revenue(db_path=DB_PATH):
    if not db_path.is_file():
        raise FileNotFoundError(f"Missing lesson database: {db_path}")
    query = """
    SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id
    ORDER BY revenue DESC, e.employee_id;
    """
    with closing(sqlite3.connect(db_path)) as conn:
        employee_results = pd.read_sql_query(query, conn)
    return employee_results


def main():
    employee_results = load_employee_revenue()
    print(employee_results)
    employee_results.to_csv(HERE / "employee_results.csv", index=False)
    ax = employee_results.plot.bar(
        x="last_name", y="revenue", figsize=(10, 6),
        color="steelblue", edgecolor="black", legend=False,
        title="Total Revenue by Employee Last Name",
    )
    ax.set_xlabel("Employee Last Name")
    ax.set_ylabel("Revenue ($)")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig(HERE / "employee_revenue_by_last_name.png")
    plt.show()


if __name__ == "__main__":
    main()
