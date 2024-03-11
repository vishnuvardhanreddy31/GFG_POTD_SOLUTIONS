class Solution:
    def countPairs(self, mat1, mat2, n, x):
        sz = n * n
        l, r = 0, sz - 1
        cnt = 0

        while l < sz and r >= 0:
            sum_val = mat1[l // n][l % n] + mat2[r // n][r % n]

            if sum_val == x:
                l += 1
                r -= 1
                cnt += 1
            elif sum_val > x:
                r -= 1
            else:
                l += 1

        return cnt
