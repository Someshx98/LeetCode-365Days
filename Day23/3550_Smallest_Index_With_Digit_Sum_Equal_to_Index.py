def smallestIndex(nums: list[int]) -> int:
    def sumOfDigits(x: int) -> int:
        res = 0
        while x > 0:
            res += x % 10
            x //= 10

        return res

    for i, num in enumerate(nums):
        if sumOfDigits(num) == i:
            return i

    return -1

ls = [1, 3, 2]
print(smallestIndex(ls))