class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        count = [0] * 31

        for num in nums:
            for bin in range(31):
                if num >> bin & 1:
                    count[bin] += 1

        result = 0

        for _ in range(k):
            current = 0
            for bin in range(31):
                if count[bin] > 0:
                    current |= 1 << bin
                    count[bin] -= 1

            result = (result + current ** 2) % modulo

        return result