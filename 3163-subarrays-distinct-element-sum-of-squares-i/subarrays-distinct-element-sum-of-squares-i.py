class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sz = len(nums)
        subarrays = []
        for i in range(sz):
            for j in range(i + 1, sz + 1):
                subarrays.append(nums[i : j])

        size_subarray = []

        for subarray in subarrays:
            size_subarray.append(len(set(subarray)))

        result = [x ** 2 for x in size_subarray]

        return sum(result)