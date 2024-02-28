class Solution:
    def DivisibleByEight(self, s):
        # Remove non-numeric characters from the string
        s = ''.join(c for c in s if c.isdigit())

        # Check if the cleaned string is empty
        if not s:
            return -1  # If the string becomes empty after removing non-numeric characters, it's not divisible by 8

        # Check if the entire string is less than 4 digits
        if len(s) < 4:
            if int(s) % 8 == 0:
                return 1  # divisible by 8
            else:
                return -1  # not divisible by 8
        else:
            # Check the last three digits of the cleaned string
            num = int(s[-3:])
            if num == 0 or num % 8 == 0:
                return 1  # divisible by 8
            else:
                return -1  # not divisible by 8