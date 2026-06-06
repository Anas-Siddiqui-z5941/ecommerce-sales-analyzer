from utils import load_data, clean_data
from pathlib import Path

from analysis import (
    calculate_metrics,
    top_selling_product,
    highest_revenue_category,
    most_sold_category
)


def main():

    df = load_data("C:/Users/ASUS/ml-journey/mini-projects/ecommerce-sales-analyzer/data/sales.csv")

    df = clean_data(df)

    total_revenue, avg_order = calculate_metrics(df)

    top_product = top_selling_product(df)

    top_revenue_category = highest_revenue_category(df)

    top_sold_category = most_sold_category(df)

    print("\n===== E-COMMERCE SALES REPORT =====")

    print(f"Total Revenue: ₹{total_revenue}")

    print(f"Average Order Value: ₹{avg_order:.2f}")

    print(f"Top Selling Product: {top_product}")

    print(f"Highest Revenue Category: {top_revenue_category}")

    print(f"Most Sold Category: {top_sold_category}")

    BASE_DIR = Path(__file__).parent

    report_path = BASE_DIR / "report.txt"

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("===== E-COMMERCE SALES REPORT =====\n")

        file.write(f"Total Revenue: Rs.{total_revenue}\n")

        file.write(f"Average Order Value: Rs.{avg_order:.2f}\n")

        file.write(f"Top Selling Product: {top_product}\n")

        file.write(
            f"Highest Revenue Category: {top_revenue_category}\n"
        )

        file.write(
            f"Most Sold Category: {top_sold_category}\n"
        )


if __name__ == "__main__":
    main()