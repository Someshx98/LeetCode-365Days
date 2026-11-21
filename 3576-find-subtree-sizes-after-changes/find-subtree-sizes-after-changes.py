class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        ans = [1] * n
        last = {}

        def dfs(x, p):
            prev = last.get(s[x])
            np_ = prev if prev is not None else p
            last[s[x]] = x
            for y in g[x]:
                dfs(y, x)
            last[s[x]] = prev
            if x:
                ans[np_] += ans[x]

        dfs(0, -1)
        return ans