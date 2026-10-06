import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.copy()
    result = []

    for prod in sales["product_id"].unique():
        rows = sales.loc[sales["product_id"] == prod]
        first_year = rows["year"].min()
        result.append(rows[rows["year"] == first_year])

    out = pd.concat(result)
    return out[["product_id", "year", "quantity", "price"]].rename(
        columns={"year": "first_year"}
    )

data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sell = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})

print(sales_analysis(sales=sell))