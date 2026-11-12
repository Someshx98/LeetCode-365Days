class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_counter = 1
        dec_counter = 1
        best_counter = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_counter += 1
                dec_counter = 1

            elif nums[i] < nums[i - 1]:
                inc_counter = 1
                dec_counter += 1

            else:
                inc_counter = 1
                dec_counter = 1

            best_counter = max(inc_counter, dec_counter, best_counter)

        return best_counter