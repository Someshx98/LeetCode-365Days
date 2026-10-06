import pandas as pd

data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'], [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'], [7, 4, '2019-08-09', '2019-08-09']]
delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})

print(delivery)

cus = []
im_sc = []

for i in delivery["customer_id"]:
    if i not in cus:
        cus.append(i)
        customer_rows = delivery[delivery["customer_id"] == i].sort_values(by = "order_date")
        order_date = customer_rows["order_date"].iloc[0]
        pref_date = customer_rows["customer_pref_delivery_date"].iloc[0]

        if order_date == pref_date:
            im_sc.append("immediate")
        else:
            im_sc.append("scheduled")

print(im_sc)
print(cus)

x = round((im_sc.count("immediate") / len(im_sc)) * 100, 2)

print(
pd.DataFrame({
    "immediate_percentage" : [x]
})
)