def minElement(nums: list[int]) -> int:
    if not nums:
        return 0

    def digitSum(x):
        sum = 0
        while x:
            sum += x % 10
            x //= 10
        return sum

    mid_res = []

    for num in nums:
        mid_res.append(digitSum(num))

    return min(mid_res)

ar = [999,19,199]

print(minElement(ar))