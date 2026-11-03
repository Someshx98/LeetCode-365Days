class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum_element = max(nums)
        list_moves = [maximum_element - num for num in nums]

        return sum(list_moves)