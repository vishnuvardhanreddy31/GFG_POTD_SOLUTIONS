class Solution:   
    def peakElement(self,arr, n):
        # Code here
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            
            if arr[mid]>arr[mid+1]:
                right=mid
                
            else:
                left=mid+1
        return left
        