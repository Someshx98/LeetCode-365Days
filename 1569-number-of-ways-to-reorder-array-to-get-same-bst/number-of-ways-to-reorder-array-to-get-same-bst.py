from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10 ** 9 + 7

        def count(arr):
            size = len(arr)

            if size <= 2:
                return 1

            root = arr[0]
            left_sub_tree = []
            right_sub_tree = []

            for i in range(1, size):
                if arr[i] < root:
                    left_sub_tree.append(arr[i])

                if arr[i] > root:
                    right_sub_tree.append(arr[i])

            left_ways = count(left_sub_tree)
            right_ways = count(right_sub_tree)

            final_count = comb(len(left_sub_tree) + len(right_sub_tree), len(left_sub_tree))

            return (final_count * left_ways * right_ways) % mod

        return (count(nums) - 1) % mod