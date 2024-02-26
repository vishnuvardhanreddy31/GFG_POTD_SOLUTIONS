# All Possible Strings Subsequences

## 26-02-23

## Problem Statement

Given a string `s` of length n, find all the possible subsequences of the string `s` in lexicographically-sorted order.

## Example

### Input:

```
s = "abc"
```

### Output:

```
['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
```

## Constraints

- 1 <= n <= 16
- `s` will constitute lower case English alphabets.

## Expected Time Complexity

```
O(n * 2^n)
```

## Expected Space Complexity

```
O(n * 2^n)
```

## Python Solution

```python
class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		def solve(s,n,i,ans):
		    if i==len(s):
		        if n!="":
		            ans.append(n)
		            n=""
		    else:
		        solve(s,n+s[i],i+1,ans)
		        solve(s,n,i+1,ans)
		ans=[]
		solve(s,"",0,ans)
		ans.sort()
		return ans
```
