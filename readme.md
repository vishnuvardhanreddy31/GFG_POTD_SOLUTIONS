# String Duplicate Removal

## 10-03-2024

## Problem Statement

Given a string `str` which may contain lowercase and uppercase characters, the task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be the same as in the original string.

## Examples

### Example 1:

Input:

```
str = "geEksforGEeks"
```

Output:

```
"geEksforG"
```

Explanation: After removing duplicate characters such as E, e, k, s, we have a string as "geEksforG".

### Example 2:

Input:

```
str = "HaPpyNewYear"
```

Output:

```
"HaPpyNewYr"
```

Explanation: After removing duplicate characters such as e, a, we have a string as "HaPpyNewYr".

## Constraints

- 1 ≤ N ≤ 10^5
- String contains uppercase and lowercase English letters.

## Expected Time Complexity

O(N)

## Expected Auxiliary Space

O(N)

## Python Solution

```python
class Solution:
	def removeDuplicates(self,str):
	    # code here
	    str_set=set()
	    new_str=""
	    for i in str:
	        if i not in str_set:
	            new_str+=i
	            str_set.add(i)
	    return new_str
```
