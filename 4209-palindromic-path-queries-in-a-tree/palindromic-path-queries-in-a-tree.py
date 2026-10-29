class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        cur = [1 << (ord(c) - 97) for c in s]
    
        timer = 0
        stack = [(0, -1, 0)]
        up[0][0] = 0
        base[0] = cur[0]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        up[0][v] = u
                        depth[v] = depth[u] + 1
                        base[v] = base[u] ^ cur[v]
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1
    
        for k in range(1, LOG):
            prev, row = up[k - 1], up[k]
            for v in range(n):
                row[v] = prev[prev[v]]
    
        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return up[0][a]
    
        bit = [0] * (n + 2)
    
        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i
    
        def pref(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r
    
        def P(x):
            return base[x] ^ pref(tin[x])
    
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), 1 << (ord(parts[2]) - 97)
                d = cur[u] ^ c
                if d:
                    cur[u] = c
                    add(tin[u], d)
                    add(tout[u] + 1, d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = P(u) ^ P(v) ^ cur[l]
                ans.append(mask & (mask - 1) == 0)
        return ans