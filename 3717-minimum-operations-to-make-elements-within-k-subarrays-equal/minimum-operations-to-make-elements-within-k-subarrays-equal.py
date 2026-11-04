class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, dc, ds):
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def query(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        LOG = 1
        while LOG * 2 <= m:
            LOG *= 2

        def kth(target):
            pos = 0
            pw = LOG
            while pw:
                nxt = pos + pw
                if nxt <= m and cnt[nxt] < target:
                    pos = nxt
                    target -= cnt[nxt]
                pw >>= 1
            return pos + 1

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth((x + 1) // 2)
                med = vals[r - 1]
                c_le, s_le = query(r)
                cost[i - x + 1] = (med * c_le - s_le) + (total - s_le) - med * (x - c_le)

        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]