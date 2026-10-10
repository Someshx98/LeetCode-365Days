class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff_list = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]

        if sum(diff_list) <= k:
            return 0

        max_diff = max(diff_list)
        count = [0] * (max_diff + 1)

        for d in diff_list:
            count[d] += 1

        for v in range(max_diff, 0, -1):
            if count[v] == 0:
                continue
            if count[v] <= k:
                k -= count[v]
                count[v - 1] += count[v]
                count[v] = 0

            else:
                count[v - 1] += k
                count[v] -= k
                k = 0
                break

        return sum(c * v * v for v, c in enumerate(count))