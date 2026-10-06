n = int(input("Enter the size of the array: "))
nums = [int(input("Enter the element: ")) for _ in range(n)]

subsets = [[]]

for num in nums:
    subsets += [current + [num] for current in subsets]

print(subsets)