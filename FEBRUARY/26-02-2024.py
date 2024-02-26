class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		def solve(s,n,i,ans):
		    if i==len(s):
		        if n!="":
		            ans.append(n)
		            n=""
		    else:
		        solve(s,n+s[i],i+1,ans)
		        solve(s,n,i+1,ans)
		ans=[]
		solve(s,"",0,ans)
		ans.sort()
		return ans