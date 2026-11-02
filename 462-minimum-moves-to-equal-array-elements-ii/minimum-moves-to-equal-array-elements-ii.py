class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        x, y = 0, len(nums) - 1
        moves = 0
        while x < y:
            moves += nums[y] - nums[x]
            x += 1
            y -= 1
    
        return moves