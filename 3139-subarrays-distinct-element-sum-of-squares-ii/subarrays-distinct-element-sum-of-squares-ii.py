class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        size = len(nums)
        s = [0] * (4 * size)
        sq = [0] * (4 * size)
        lazy = [0] * (4 * size)
    
        def apply(o, length, v):
            sq[o] += 2 * v * s[o] + v * v * length
            s[o] += v * length
            lazy[o] += v
    
        def update(o, l, r, L, R):
            if L <= l and r <= R:
                apply(o, r - l + 1, 1)
                return
            m = (l + r) // 2
            if lazy[o]:
                apply(2 * o, m - l + 1, lazy[o])
                apply(2 * o + 1, r - m, lazy[o])
                lazy[o] = 0
            if L <= m:
                update(2 * o, l, m, L, R)
            if R > m:
                update(2 * o + 1, m + 1, r, L, R)
            s[o] = s[2 * o] + s[2 * o + 1]
            sq[o] = sq[2 * o] + sq[2 * o + 1]
    
        last = {}
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, j)
            last[x] = j
            ans += sq[1]
        return ans % mod