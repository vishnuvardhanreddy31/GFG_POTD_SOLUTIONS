# User function Template for python3
#Sum of bit differences 
#29-02-2024
class Solution:
    def sumBitDifferences(self, arr, n):
        ans = 0
        for i in range(0, 32):
            count = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count += 1
            ans += (count * (n - count) * 2)

        return ans
