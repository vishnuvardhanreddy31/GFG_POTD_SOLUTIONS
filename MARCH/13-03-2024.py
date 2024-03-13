class Solution:
    def matrixDiagonally(self,mat):
        # code here
        from collections import defaultdict

        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])

        ans = []
        for k in sorted(d):
            if k&1:
                ans.extend(d[k])
            else:
                ans.extend(d[k][::-1])
        return ans