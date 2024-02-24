class Solution:
    def maxSum(self, n): 
        # code here 
        
        dp=[-1 for _ in range(n+1)]
        
        def helper(n,dp):
            if n==0 or n==1 :
                return n
            if dp[n]!=-1:
                return dp[n]
            else:
                dp[n]=max(n,helper(n//3,dp)+helper(n//2,dp)+helper(n//4,dp))
                return dp[n]
                
        return helper(n,dp)