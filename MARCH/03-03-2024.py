from functools import cmp_to_key

class Solution:
    def printLargest(self, n, array):
        def custom_compare(x, y):
            xy = x + y
            yx = y + x
            return (xy > yx) - (xy < yx)

        array.sort(key=cmp_to_key(custom_compare), reverse=True)

        return "".join(map(str, array))
