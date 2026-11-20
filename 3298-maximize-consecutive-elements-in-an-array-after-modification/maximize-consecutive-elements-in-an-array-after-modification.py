class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}

        for num in nums:
            len_without_inc = dp.get(num - 1, 0) + 1
            len_with_inc = dp.get(num, 0) + 1
            
            dp[num + 1] = max(dp.get(num + 1, 0), dp.get(num, 0) + 1)
            dp[num] = max(dp.get(num, 0), dp.get(num - 1, 0) + 1)
        return max(dp.values()) if dp else 0