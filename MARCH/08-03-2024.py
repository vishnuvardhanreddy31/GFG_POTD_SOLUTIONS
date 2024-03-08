class Solution:
    def sameFreq(self, s):
        cnt = {}
        for char in s:
            cnt[char] = cnt.get(char, 0) + 1
        
        nin = nax = cnt[s[0]]

        for char, freq in cnt.items():
            nin = min(nin, freq)
            nax = max(nax, freq)
            if nax - nin > 1:
                return 0

        cnin = sum(1 for freq in cnt.values() if freq == nin)

        return len(cnt) - cnin <= 1