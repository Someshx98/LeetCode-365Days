def minimumOperations(nums: list[int]) -> int:
    count = 0

    for num in nums:
        if num % 3 == 0:
            continue

        else:
            num -= num % 3
            count += 1

    return count

p = [1,2,3,4]

print(minimumOperations(p))