class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        size = len(nums)

        if size <= 1:
            return 0

        def digit_sum(num):
            add = 0

            while num > 0:
                add += num % 10
                num //= 10

            return add

        order = sorted(range(size), key = lambda i: (digit_sum(nums[i]), nums[i]))
        
        visited = [False] * size

        res = 0

        for i in range(size):
            if visited[i] or order[i] == i:
                continue

            cycle = 0

            j = i

            while not visited[j]:
                visited[j] = True
                j = order[j]
                cycle += 1

            res += cycle - 1

        return res