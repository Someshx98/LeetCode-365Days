import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
work = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

target = int(input("Enter the value of n: "))

# print(work)

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column_name = f"getNthHighestSalary({N})"
    if N <= 0:
        return pd.DataFrame({
            column_name : [None]
        })

    dist = employee['Salary'].drop_duplicates().sort_values(ascending=False)

    if N > len(dist):
        return pd.DataFrame({
            column_name : [None]
        })

    nth = dist.iloc[N-1]

    return pd.DataFrame({
        column_name : [nth]
    })

print(nth_highest_salary(work, target))