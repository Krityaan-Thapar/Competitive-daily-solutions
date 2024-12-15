# Question 

_Difficulty: Easy_

You have been given two arrays/lists 'ARR1' and 'ARR2' of length 'N'. Your task is to pair each element of 'ARR1' to an element of 'ARR2' such that the sum of the absolute difference of all pairs is minimum.
Example:

If 'ARR1' = [0, 2, 1], and 'ARR2' = [8, 10, 4] then the most optimal pairing will be (0, 4) , (1, 8) and (2, 10). The sum of absolute difference will be 4 + 7 + 8 = 19.

Note:
An element from one array can make a pair only with at most one element of another array.

**Examples :**
```
Sample Input 1:
1
5
10 24 5 90 4 
14 2 32 5 6 

Sample output 1:
74

Explanation of Sample output 1:
The best way to pair the elements is (4, 2), (5, 5), (10,6), (24, 14), (90, 32). The sum of the absolute difference between pairs is  2 + 0 + 4 + 10 + 58 = 74 

Sample Input 2:
2
4 
1 2 3 1
4 5 5 4
5
1 1 1 1 1
1 1 1 1 1

Sample output 2:
11
0
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 5000
0 <= ARR1[i] <= 10^5
0 <= ARR2[i] <= 10^5

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/minimum-sum-of-absolute-difference_973294?leftPanelTabValue=SOLUTION

## Daily History
- Dec 16, 2024