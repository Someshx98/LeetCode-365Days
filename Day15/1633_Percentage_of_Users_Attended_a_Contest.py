import pandas as pd

data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]
register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})

print(users)
print(register)

contests = []
people = users["user_id"].unique().tolist()
percentage = []

# for _, row in register.iterrows():
#

for contest in register["contest_id"]:
    if contest not in contests:
        contests.append(contest)
        con_user_row = register[register["contest_id"] == contest]
        user_attended = con_user_row["user_id"]
        p = 0

        for x in user_attended:
            if x in people:
                p += 1

        percentage.append(
            round(
                p / len(people) * 100,
                2
            )
        )

result = pd.DataFrame({
    "contest_id" : contests,
    "percentage" : percentage
})

print(result)

result.sort_values(by = ["percentage", "contest_id"], ascending = [False, True], inplace = True)
print(result)