class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        def solve(s, current, index, result):
            if index == len(s):
                if current != "":
                    result.append(current)
                    current = ""
            else:
                solve(s, current + s[index], index + 1, result)
                solve(s, current, index + 1, result)

        result = []
        solve(s, "", 0, result)
        result.sort()
        return result
