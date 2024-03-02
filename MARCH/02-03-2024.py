from collections import OrderedDict

class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        num_map=OrderedDict()
        for i in a:
            if i not in num_map:
                num_map[i]=1
            else:
                num_map[i]+=1
        
            if num_map[i]==k:
                return i
        else:
            return -1