def pivotArray(nums: list[int], pivot: int) -> list[int]:
    left = []
    right = []
    equal = []
    result = []

    for num in nums:
        if num == pivot:
            equal.append(num)
        if num > pivot:
            right.append(num)
        if num < pivot:
            left.append(num)

    result.extend(left)
    result.extend(equal)
    result.extend(right)

    return result


arr = [-3,4,3,2]
p = 2

print(pivotArray(arr, p))