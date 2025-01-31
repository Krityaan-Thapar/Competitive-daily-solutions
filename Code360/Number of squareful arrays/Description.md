# Question 

_Difficulty: Hard_

You are given an Array/List Arr of non-negative integers. Your task is to return the number of Squareful permutations of the array.
An array is called Squareful if the sum of every pair of adjacent elements is a perfect square.

Example
ARR[1,3,6] is a Squareful array as 1+3=4 i.e. 2^2 , 3+6=9 i.e. 3^2.
Two permutations ARR1 and ARR2, are different from each other if there exit an index i such that ARR1[i] != ARR2[i].

Example:
[1,6,3] and [6,1,3] are different permutations.

**Examples :**
```
Sample input 1
3
1 24 3

Sample output 1
2

Sample input explanation
Different permutations of [1, 24, 3] are - [1, 24, 3] , [1, 3, 24] , [24, 1, 3] , [24, 3, 1] , [3, 1, 24] , [3, 24, 1].
Out of which [24, 1, 3] (24 + 1 = 25, 1 + 3 = 4) and [3, 1, 24] (3 + 1 = 4, 1 + 14 = 25) are Squareful.

Sample input 2
4
1 1 1 1

Sample output 2:-
0
```

**Constraints:**
```
1 <= N <= 12
0 <= ARR[i] <= 10^4 , where 0 <= i < N

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/number-of-squareful-arrays_1235194?leftPanelTabValue=SOLUTION

## Daily History
- Jan 31, 2025