import random as rd

def fact (n):
    if n == 0:
        return 1
    return n * fact(n-1)

result = []

size = int(input("Enter the size of the array: "))
nums = [int(input("Enter the element: ")) for _ in range(size)]

while len(result) != fact(size):
    temp = []
    while len(temp) < size:
        x = rd.choice(nums)
        if x not in temp:
            temp.append(x)

    if temp not in result:
        result.append(temp)

print(result)