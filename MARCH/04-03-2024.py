class Solution:
	def swapElements(self, arr, n):
	    #Code heren-2
	    if n>=2:
	        for i in range(n-2):
	            arr[i],arr[i+2]=arr[i+2],arr[i]