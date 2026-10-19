class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums_sorted = sorted(nums)
        result = []

        for i, num in enumerate(nums_sorted):
            if num == target:
                result.append(i)

        return result