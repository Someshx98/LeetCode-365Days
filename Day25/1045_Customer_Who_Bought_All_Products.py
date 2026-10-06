import pandas as pd

data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})

print(customer)
print(product)

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    mid = customer[['customer_id', 'product_key']].drop_duplicates()
    mid.columns = ["Cus", "Pro"]

    grouped = mid.groupby("Cus")

    res = []
    product_set = set(product["product_key"])

    for key, value in grouped:
        if set(value["Pro"]) == product_set:
            res.append(key)

    return pd.DataFrame({"customer_id": res})

print(find_customers(customer, product))