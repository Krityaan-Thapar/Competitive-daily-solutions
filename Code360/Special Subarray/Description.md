# Question 

_Difficulty: Moderate_

You are given an array ‘ARR’ of size ‘N’. Your task is to find the special subarray of ‘ARR’. A special subarray is the smallest contiguous part of an array that contains all the occurrences of the most frequent element of the array.
For example:

You are given ‘ARR’ = {1, 3, 4, 3, 5}. Then our answer will be {3, 4, 3} because the most frequent element is 3, and the subarray {3, 4, 3} contains all the occurrences of 3.

**Examples :**
```
Sample Input 1:
2
5
1 3 4 3 5
5
0 2 4 4 7

Sample Output 1:
3 4 3
4 4

Explanation:
For the first test case, you are given arr = {1, 3, 4, 3, 5}. Then our answer will be {3, 4, 3} because the most frequent element is 3, and the subarray {3, 4, 3} contains all the occurrences of 3.
For the second test case, you are given arr = {0, 2, 4, 4, 7}. Then our answer will be {4, 4} because the most frequent element is 3, and the subarray {4, 4} contains all the occurrences of 4.

Sample Input 2:
2
4
1 2 1 1 
6
4 5 6 8 8 8

Sample Output 2:
1 2 1 1
8 8 8
```

**Constraints:**
```
1 <= T <= 10 
1 <= N  <= 5000
0 <= ARR[i] <= 10 ^ 6

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/special-subarray_2825008?leftPanelTabValue=SOLUTION

## Daily History
- Dec 13, 2024