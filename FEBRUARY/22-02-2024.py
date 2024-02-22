
#Distinct occurrences
#Author : Goli Vishnuvardhan Reddy
#Approach : DP
class Solution:
    def sequenceCount(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def help(i, j):
            if j == m:
                return 1
            if i == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            a = help(i + 1, j)
            b = 0
            if s[i] == t[j]:
                b = help(i + 1, j + 1)

            dp[i][j] = (a + b) % (10**9 + 7)
            return dp[i][j]

        return help(0, 0)