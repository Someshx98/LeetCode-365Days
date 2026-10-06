def leftRightDifference(nums: list[int]) -> list[int]:
    n = len(nums)
    left = [0] + nums[: -1]
    right = nums[1:] + [0]
    count_left = 0
    count_right = 0
    left_sum = []
    right_sum = []
    for l in left:
        count_left += l
        left_sum.append(count_left)

    for r in right[::-1]:
        count_right += r
        right_sum.append(count_right)

    right_sum = right_sum[::-1]
    result = []

    for i in range(n):
        result.append(abs(right_sum[i] - left_sum[i]))

    return result

x = [10,4,8,3]

print(leftRightDifference(x))
