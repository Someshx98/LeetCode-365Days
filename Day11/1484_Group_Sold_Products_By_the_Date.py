import pandas as pd

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

print(activities)

print(activities["sell_date"].value_counts())

unique_activities =activities.drop_duplicates().reset_index(drop = True)

print(unique_activities)

print(unique_activities["sell_date"].value_counts())

dates = unique_activities["sell_date"].unique().tolist()
print(dates)

p = []

for date in dates:
    prod = unique_activities[
        unique_activities["sell_date"] == date
    ]["product"].tolist()

    p.append(prod)

    print(prod)

print(p)

print(unique_activities["sell_date"].value_counts().tolist())

result = pd.DataFrame({
    "sell_date" : unique_activities["sell_date"].unique().tolist(),
    "num_sold" : unique_activities["sell_date"].value_counts().tolist(),
    "products" : p
})

print(result)