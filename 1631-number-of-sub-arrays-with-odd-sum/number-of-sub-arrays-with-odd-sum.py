class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10 ** 9 + 7
        even, odd, prefix, count = 1, 0, 0, 0

        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                count += odd
                even += 1

            else:
                count += even
                odd += 1

        return count % mod