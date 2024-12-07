# Question 

_Difficulty: Hard_

You are given a string “str”. Find the maximum number of non-empty substrings of “str” such that no two substrings overlap with each other and each substring that you select containing a letter ‘t’ must contain all the occurrences of ‘t’ in that substring.
A string ‘a’ is a substring of a string ‘b’ if ‘a’ can be obtained from ‘b’ by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.
Note:
If there are multiple solutions of a string, return the string with minimum total length.

For Example :
Let str = abaccce
Now In this example, we can make a maximum of three substrings i.e. {‘b’, ‘ccc’, ‘e’}.

Note:
There can be one more solution with maximum substrings equal to three i.e. {‘aba’, ‘ccc’, ‘e’} but we have to select the substrings with minimum total length. So the final answer is  {‘b’, ‘ccc’, ‘e’}.

**Examples :**
```
Sample Input 1:
2
ab
wxzxzz

Sample Output 1:
a b
w xzxzz

Explanation For Sample Output 1 :
For the first test case, there are two non-overlapping substrings satisfying the condition i.e. a, b.
For the second test case, we have to select the whole substring “xzxzz” for the final answer as we need to select all the occurrences of a letter in one substring. Hence the answer is w, xzxzz.

Sample Input 2:
2
abc
xtx

Sample Output 2:
a b c
t
```

**Constraints:**
```
1 <= T <= 10
1 <= |str| <= 10^5, where |str| represents the length of the String str.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/non-overlapping-substrings_2179629?leftPanelTabValue=SOLUTION
https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/solutions/743223/c-java-greedy-o-n/

## Daily History
- Dec 7, 2024