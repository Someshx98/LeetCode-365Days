import pandas as pd

data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})

print(prices)
print(units_sold)

merged = pd.merge(prices, units_sold, on="product_id", how="left")

valid = merged[
        (
            (merged["purchase_date"] >= merged["start_date"])
            & (merged["purchase_date"] <= merged["end_date"])
        )
        | merged["purchase_date"].isna()
    ].copy()

valid["revenue"] = valid["price"] * valid["units"].fillna(0)
valid["units"] = valid["units"].fillna(0)

grouped = valid.groupby("product_id", as_index=False).agg(
    total_revenue=("revenue", "sum"), total_units=("units", "sum")
)

grouped["average_price"] = (
    (grouped["total_revenue"] / grouped["total_units"])
    .fillna(0)
    .round(2)
)

result = prices[["product_id"]].drop_duplicates().merge(
    grouped[["product_id", "average_price"]], on="product_id", how="left"
)

result["average_price"] = result["average_price"].fillna(0)

print(result)