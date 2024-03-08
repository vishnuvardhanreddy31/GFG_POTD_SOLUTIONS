## Check if frequencies can be equal

## 08-03-2024

Given a string `s` consisting of only lower alphabetic characters, your task is to determine whether it is possible to remove at most one character from the string in such a way that the frequency of each distinct character becomes the same. If possible, the function should return `true`; otherwise, it should return `false`.

### Example

**Input:**

```
s = "xyyz"
```

**Output:**

```
1
```

**Explanation:**
Removing one `y` will make the frequency of each character equal.

**Input:**

```
s = "xxxxyyzz"
```

**Output:**

```
0
```

**Explanation:**
The frequency cannot be made the same by removing at most one character.

### Your Task

You are required to complete the function `sameFreq()`, which takes a string as an input parameter and returns a boolean value denoting whether the same frequency is possible or not.

### Constraints

- 1 <= |s| <= 10^5

### Expected Complexity

- Time Complexity: O(|s|)
- Auxiliary Space: O(1)

<h3>Python Solution</h3>

```python

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

```

Good luck, and happy coding😊!
