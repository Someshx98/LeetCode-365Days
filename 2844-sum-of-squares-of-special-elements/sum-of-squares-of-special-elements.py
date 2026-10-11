class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res_list = []
        nums_size = len(nums)

        for i in range(nums_size):
            if nums_size % (i + 1) == 0:
                res_list.append(nums[i] ** 2)

        return sum(res_list)