import pandas as pd

data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})

print(queries)

p = []
quality = []
pp = []

for pet in queries["query_name"]:
    if pet not in p:
        p.append(pet)
        print(pet)

        pet_rows = queries[queries["query_name"] == pet]
        print(pet_rows)

        q = 0
        times = 0

        for _, row in pet_rows.iterrows():
            q += row["rating"] / row["position"]

            if row["rating"] < 3:
                times += 1

        t = round(q / len(pet_rows), 2)

        quality.append(t)

        pp.append(
            round(
                (times / len(pet_rows)) * 100,
                2
            )
        )

print(quality)
print(pp)