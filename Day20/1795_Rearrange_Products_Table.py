import pandas as pd

data = [[0, 95, 100, 105], [1, 70, None, 80]]
groc = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # product_id = []
    # store = []
    # price = []
    #
    # for _, row in products.iterrows():
    #     p_id = row["product_id"]
    #
    #     if pd.notna(row["store1"]):
    #         product_id.append(p_id)
    #         store.append("store1")
    #         price.append(row["store1"])
    #
    #     if pd.notna(row["store2"]):
    #         product_id.append(p_id)
    #         store.append("store2")
    #         price.append(row["store2"])
    #
    #     if pd.notna(row["store3"]):
    #         product_id.append(p_id)
    #         store.append("store3")
    #         price.append(row["store3"])
    #
    # return pd.DataFrame({"product_id": product_id, "store": store, "price": price})

    result = pd.melt(
        products,
        id_vars = ["product_id"],
        value_vars = ["store1", "store2", "store3"],
        var_name = "store",
        value_name = "price"
    )

    return result.dropna(subset = ["price"])

print(rearrange_products_table(groc))