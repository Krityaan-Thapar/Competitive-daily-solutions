# Question 

_Difficulty: Hard_

You are given an array ARR of ‘N’ Integers and an integer. Your task is to divide this array into ‘K’ subsets satisfying the following constraints-

1. Each element in ARR belongs to exactly one subset.
2. All the elements in a subset are unique.
3. Each subset has a size of ‘N’/ ’K’

Your task is to find the minimum cost of constructing the ‘K’ subset.

Cost of the construction of subsets is calculated as the sum of the maximum - the minimum of a subset. If there is no way to divide ARR into K subsets satisfying the constraints, print -1.

It is guaranteed that ‘K’ is a divisor of ‘N’.

For example :

[1,2,3,1,2,5] k=2
[[1,2,3],[1,2,5]] is a valid subset division. All the elements in each subset are unique and the the cost of construction is (3 - 1) + (5 - 1) = 6  

**Examples :**
```
Sample Input 1:
2 
4 2
1 4 5 9
5 5
1 2 3 4 5

Sample Output 1:
7
0

Explanation of Sample Input 1 :
For the first test case [[1,4], [5,9]] is the required distribution.
ANS = ( 4 - 1) + (9 - 5) = 7
[ [1, 5], [9, 4] ] is also the valid distribution but the cost of construction is not minimum. 
For the second test case each subset has exactly one element [ [1], [2], [3], [4], [5] ]
ANS = (1 - 1) + (2 - 2) + (3 - 3) + (4 - 4) + (5 - 5)

Sample Input 2 :
2
6 3 
3 3 3 1 11 4
4 2 
7 11 7 11 

Sample Output 2 :
11
8
```

**Constraints:**
```
1 <= T <= 5
1 <= N <= 12
1 <= K <= N
1<= ARR[i] <= 20    
K is a devisor of the N
```

### Editorial
https://www.naukri.com/code360/problems/minimum-costs-of-subsets_1460383?leftPanelTabValue=SOLUTION

## Daily History
- Nov 20, 2024