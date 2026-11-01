class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # size = len(nums)
        # count = 0

        # while len(set(nums)) != 1:
        #     sorted_nums = sorted(nums)
        #     for i in range(size - 1):
        #         sorted_nums[i] += 1
        #     nums = sorted_nums
        #     count += 1

        # return count

        return sum(nums) - len(nums) * min(nums)