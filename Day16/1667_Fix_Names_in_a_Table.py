import pandas as pd

data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

print(users)

def fix_names(user) -> pd.DataFrame:
    user["name"] = user["name"].str.capitalize()
    return user.sort_values(by='user_id', ascending=True).reset_index(drop=True)

print(fix_names(users))