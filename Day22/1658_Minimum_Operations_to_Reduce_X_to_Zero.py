numbers = [1, 1, 4, 2, 3]

def minOperations(nums: list[int], x: int) -> int:
    target = sum(nums) - x

    if target < 0:
        return -1
    if target == 0:
        return len(nums)

    left = 0
    curr = 0
    longest = -1

    for right, num in enumerate(nums):
        curr += num

        while curr > target:
            curr -= nums[left]
            left += 1

        if curr == target:
            longest = max(longest, right - left + 1)

    return len(nums) - longest if longest != -1 else -1

print(minOperations(numbers, 5))

# numbers = [1, 1, 4, 2, 3]
#
# def minOperations(nums: list[int], x: int) -> int:
#     n = len(nums)
#     targets = []
#
#     for i in range(n + 1):
#         left_sum = sum(nums[:i])
#         if left_sum > x:
#             break
#
#         for j in range(n - i + 1):
#             total = left_sum + sum(nums[n - j:])
#             if total == x:
#                 targets.append(i + j)
#             if total > x:
#                 break
#
#     return min(targets) if targets else -1
#
# print(minOperations(numbers, 5))  # 2