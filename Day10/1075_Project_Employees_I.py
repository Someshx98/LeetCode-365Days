import pandas as pd

data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(
    data,
    columns=['project_id', 'employee_id']
).astype({
    'project_id': 'Int64',
    'employee_id': 'Int64'
})

data = [
    [1, 'Khaled', 3],
    [2, 'Ali', 2],
    [3, 'John', 1],
    [4, 'Doe', 2]
]

employee = pd.DataFrame(
    data,
    columns=['employee_id', 'name', 'experience_years']
).astype({
    'employee_id': 'Int64',
    'name': 'object',
    'experience_years': 'Int64'
})

value = project["project_id"].value_counts().index.tolist()

print(value)

average = []

for project_id in value:

    emp_ids = project[
        project["project_id"] == project_id
    ]["employee_id"].tolist()

    exp = employee[
        employee["employee_id"].isin(emp_ids)
    ]["experience_years"].tolist()

    # Calculate average
    avg = sum(exp) / len(exp)

    average.append(avg)


# Create final DataFrame
result = pd.DataFrame({
    "project_id": value,
    "average_years": average
})

print(result)