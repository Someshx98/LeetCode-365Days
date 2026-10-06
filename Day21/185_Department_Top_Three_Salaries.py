import pandas as pd

data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
people = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
station = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame):
    merged_df = pd.merge(employee,
                         department,
                         left_on = "departmentId",
                         right_on = "id",
                         how = "left",
                         suffixes = ("_emp", "_dep")
                         )

    merged_df["rank"] = merged_df.groupby("departmentId")["salary"].rank(method = "dense", ascending = False)

    return merged_df[
        merged_df["rank"] <= 3
    ][["name_dep", "name_emp", "salary"]].rename(columns = {
        "name_dep": "Department",
        "name_emp": "Employee",
        "salary": "Salary"
    })

print(top_three_salaries(people, station))
