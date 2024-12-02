# Question 

_Difficulty: Hard_

You are given two strings ‘A’ and ‘B’. Your task is to return a substring ‘S’ of ‘A’ such that the following conditions hold true :
• You can make ‘B’ from ‘S’ by removing some characters and rearranging some characters zero or more times.
• Length of ‘S’ must be as minimum as possible.

Note :
Testcases are generated such that a substring always exists and is unique.

Example :
A = ninjas, B = sin
All possible substrings with which 'B' can be created are
"ninjas", "injas".
Hence the substring with minimum length is "injas".

**Examples :**
```
Sample Input 1 :
fight it 

Sample Output 1 :
ight

Explanation Of Sample Input 1 :
Given A = “fight” and B = “it” 
Consider the substring “ight” of A. 
We can remove g and h from it to get “it”.
We can also get "it" from "fight" but it is not the substring with minimum length.

Sample Input 2 :
coding cin

Sample Output 2 :
codin
```

**Constraints:**
```
1 <=  |A| = |B| <= 3000
Both A, B contain only lowercase English letters.
Where |A| and |B| are the length of strings.

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/min-substring_1215004?leftPanelTabValue=SOLUTION

## Daily History
- Dec 1, 2024