class Solution:
    def largestSubsquare(self, n, a):
        col = [[0] * n for _ in range(n)]
        row = [[0] * n for _ in range(n)]

        for i in range(n):
            sum_ = 0
            for j in range(n - 1, -1, -1):
                sum_ = 0 if a[i][j] == 'O' else sum_ + 1
                col[i][j] = sum_

        for j in range(n):
            sum_ = 0
            for i in range(n - 1, -1, -1):
                sum_ = 0 if a[i][j] == 'O' else sum_ + 1
                row[i][j] = sum_

        out = 0
        for i in range(n):
            for j in range(n):
                sq = min(col[i][j], row[i][j])
                while sq > out:
                    if col[i + sq - 1][j] >= sq and row[i][j + sq - 1] >= sq:
                        out = sq
                    sq -= 1

        return out
