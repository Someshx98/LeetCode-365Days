import pandas as pd

employee = pd.DataFrame({
    "id" : [1, 2, 3, 4, 5],
    "salary" : [1000, 2000, 5000, 3000, 8000]
})

print(employee)

result = pd.DataFrame({
        "SecondHighestSalary" : [sorted(employee["salary"].sort_values(ascending=True))[-2]]
    })

print(result)