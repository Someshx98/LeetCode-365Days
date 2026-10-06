import pandas as pd

orders = pd.DataFrame({
    "order_number" : [1, 2, 3, 4],
    "customer_number" : [1, 2, 3, 3]
})

print(orders)

print(orders.customer_number.value_counts())

counts = orders.customer_number.value_counts()
print(counts.index[0])