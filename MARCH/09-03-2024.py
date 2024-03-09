class Solution:
    def nthCharacter(self, s, r, n):
        while r > 0:
            m = ""
            for i in range(min(len(s), n+1)):
                if s[i] == '1':
                    m += "10"
                else:
                    m += "01"
            
            s = m
            r -= 1
        
        return s[n]