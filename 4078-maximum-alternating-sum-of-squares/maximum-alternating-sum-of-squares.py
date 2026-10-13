class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_sum = 0
        size = len(nums)
        evens = (size + 1) // 2
    
        nums = sorted(nums, key = abs, reverse = True)
    
        array = [0] * size
    
        array[0 : : 2] = nums[:evens]
        array[1 : : 2] = nums[evens:]
    
        for i, num in enumerate(array):
            if i % 2 == 0:
                max_sum += num ** 2
            elif i % 2 == 1:
                max_sum -= num ** 2
    
        return max_sum