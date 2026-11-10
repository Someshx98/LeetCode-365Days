class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        
        dp[0] = 0
        
        for j in range(1, n + 1):

            if j - 1 >= 0:
                cost_from_prev_1 = dp[j-1] + costs[j-1] + (j - (j-1))**2
                dp[j] = min(dp[j], cost_from_prev_1)
            
            if j - 2 >= 0:
                cost_from_prev_2 = dp[j-2] + costs[j-1] + (j - (j-2))**2
                dp[j] = min(dp[j], cost_from_prev_2)
            
            if j - 3 >= 0:
                cost_from_prev_3 = dp[j-3] + costs[j-1] + (j - (j-3))**2
                dp[j] = min(dp[j], cost_from_prev_3)
                
        return dp[n]