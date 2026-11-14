class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        best = float('inf')
        for length in range(l, min(r, n) + 1):
            for i in range(n - length + 1):
                s = prefix[i + length] - prefix[i]
                if s > 0 and s < best:
                    best = s

        return best if best != float('inf') else -1