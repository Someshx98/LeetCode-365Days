import pandas as pd

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

print(courses)

classes = courses["class"].value_counts()
print(classes.index.to_list())
print(classes)

res = pd.DataFrame({
    "class": classes[classes > 5].index
})

print(res)