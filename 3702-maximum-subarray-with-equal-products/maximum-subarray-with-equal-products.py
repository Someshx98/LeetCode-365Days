from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g * l:
                    ans = max(ans, j - i + 1)
                if p > 25200:
                    break
        return ans