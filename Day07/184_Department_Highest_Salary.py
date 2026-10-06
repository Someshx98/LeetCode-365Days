import pandas as pd

employee = pd.DataFrame({
    "id" : [1, 2, 3, 4, 5],
    "name" : ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary" : [70000, 90000, 80000, 60000, 90000],
    "departmentId" : [1, 1, 2, 2, 1]
})

department = pd.DataFrame({
    "id" : [1, 2],
    "name" : ["ÏT", "Sales"]
})

print(employee)
print(department)

res = employee.merge(
    department,
    left_on="departmentId",
    right_on="id",
)

res["max_salary"] = res.groupby("departmentId")["salary"].transform("max")

res = res[res["salary"] == res["max_salary"]]

print(res)