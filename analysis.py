def calculate_metrics(df):

    df["Revenue"] = df["Price"] * df["Quantity"]

    total_revenue = df["Revenue"].sum()

    average_order_value = df["Revenue"].mean()

    return total_revenue, average_order_value


def top_selling_product(df):

    product_sales = df.groupby("Product")["Quantity"].sum()

    return product_sales.idxmax()


def highest_revenue_category(df):

    revenue_category = df.groupby("Category")["Revenue"].sum()

    return revenue_category.idxmax()


def most_sold_category(df):

    sold_category = df.groupby("Category")["Quantity"].sum()

    return sold_category.idxmax()