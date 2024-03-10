class Solution:
    def removeDuplicates(self, input_str):
        unique_set = set()
        result_str = ""

        for char in input_str:
            if char not in unique_set:
                result_str += char
                unique_set.add(char)

        return result_str
