import pandas as pd

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

print(employees)

emp = []
bonus = []

for employee_id in employees["employee_id"]:
    if employee_id not in emp:
        emp.append(employee_id)

        sal_row = employees[employees["employee_id"] == employee_id]["salary"].iloc[0]
        name_row = employees[employees["employee_id"] == employee_id]["name"].iloc[0]

        if employee_id % 2 == 0:
            bonus.append(0)

        elif employee_id % 2 == 1:
            if not name_row.startswith("M"):
                bonus.append(sal_row)
            else:
                bonus.append(0)

result = pd.DataFrame({
    "employee_id" : emp,
    "bonus" : bonus
})

print(result)