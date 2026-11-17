class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        divs = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divs[L].append(d)

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divs[L]:
                    m = L // d
                    c = 0
                    for r in range(d):
                        for t in range(m // 2):
                            if s[i + r + t * d] != s[i + r + (m - 1 - t) * d]:
                                c += 1
                    best = min(best, c)
                cost[i][j] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for e in range(2 * p, n + 1):
                for b in range(2 * (p - 1), e - 1):
                    if dp[p - 1][b] < INF:
                        dp[p][e] = min(dp[p][e], dp[p - 1][b] + cost[b][e - 1])

        return dp[k][n]