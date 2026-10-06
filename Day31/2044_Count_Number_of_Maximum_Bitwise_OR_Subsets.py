def countMaxOrSubsets(nums: list[int]) -> int:
    target = 0
    for num in nums:
        target |= num

    count = 0
    n = len(nums)

    for mask in range(1, 1 << n):
        current = 0
        for i in range(n):
            if (mask >> i) & 1:
                current |= nums[i]

        if current == target:
            count += 1

    return count

x = [2,2,2]

print(countMaxOrSubsets(x))