# Rabin-Karp Algorithm

## 06-03-2024

## Problem Statement

You are given a text string and a pattern string. Your task is to find and print the starting indices (1-based) of all occurrences of the pattern string in the text string.

### Example

#### Example 1:

**Input:**

```
text = "birthdayboy"
pattern = "birth"
```

**Output:**

```
[1]
```

**Explanation:**
The string "birth" occurs at index 1 in the text.

#### Example 2:

**Input:**

```
text = "geeksforgeeks"
pattern = "geek"
```

**Output:**

```
[1, 9]
```

**Explanation:**
The string "geek" occurs twice in the text, once at index 1 and once at index 9.

### Constraints

- 1 <= |text| <= 5 \* 10^5
- 1 <= |pattern| <= |text|

### Note

Your task is to complete the function `search()` which takes the string `text` and the string `pattern` as input and returns an array denoting the start indices (1-based) of the substring pattern in the string text.

## Explanation

Implement the Rabin-Karp algorithm to efficiently search for the pattern in the given text. The algorithm is expected to have a time complexity of O(|text| + |pattern|) and auxiliary space complexity of O(1).

## Python Solution

```python
class Solution:
    def search(self, pattern, text):
        out = []
        mod = 10
        h = len(pattern)
        n = len(text)
        hashp = 0
        hasht = 0
        p = 1

        for i in range(h - 1):
            p = (p * 26) % mod

        for i in range(h):
            hashp = ((hashp * 26) + ord(pattern[i])) % mod
            hasht = ((hasht * 26) + ord(text[i])) % mod

        for i in range(n - h + 1):
            if hashp == hasht:
                j = 0
                while j < h and pattern[j] == text[i + j]:
                    j += 1
                if j == h:
                    out.append(i + 1)

            if i < n - h:
                hasht = (26 * (hasht - ord(text[i]) * p) + ord(text[i + h])) % mod
                if hasht < 0:
                    hasht += mod

        return out

```
