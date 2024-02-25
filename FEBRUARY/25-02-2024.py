class Solution:
    def count(self, n: int) -> int:
        ways = [0] * (n + 1)
   
        # Base case (If given value is 0)
        ways[0] = 1
   
        # Consider all possible moves
        moves = [3, 5, 10]
        for i in range(3):
            for j in range(moves[i], n+1):
                ways[j] += ways[j - moves[i]]
   
        return ways[n]