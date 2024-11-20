# Question 

_Difficulty: Easy_

You are given a N * M matrix GRID. You are also given Q queries. Your task is to Perform two types of query-

1) Find the sum of the rectangular submatrix defined by the upper left corner and lower right corner for each query. The position of the upper left and lower right corner is given.

2) Change the value of the element at a given position. Position and the new value of the cell are given. 

All indexes are 0 based.
For example:

GRID =[ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0] ]
Q = 2
Update element at (3,3) to 9 
left corner = (1, 1), right corner = (2, 2)
submatrix=[ [5, 6],
            [8, 9] ]   
Answer = 28

**Examples :**
```
Sample Input 1:
2
1 4 3
7 5 3 2 
1 0 0 0 1
2 0 0 2
1 0 0 0 1
2 2 1
1 1 
1 1
1 0 0 1 1

Sample Output 1:
12 7
4

Explanation of Sample Input 1:
For the first test case, the first query submatrix is [[7, 5]]
After second query array becomes= [2, 5, 3, 2]
For third query submatrix is [[2, 5]]
For the second test case, first query submatrix is [[1, 1], [1, 1]] 

Sample Input 2:
2
2 2 3
-1 1
-1 -1
1 0 1 1 1
2 1 0 1 
1 1 0 1 1
1 1 1
0
1 0 0 0 0  

Sample Output 2:
0 0
0
```

**Constraints:**
```
1 <= T <= 5
1 <= N, M <= 1000 
1 <= Q <= 10 ^ 5
-10^4 <= GRID[i] <= 10^4
```

### Editorial
https://www.naukri.com/code360/problems/matrix-range-query-mutable_1381412?leftPanelTabValue=SOLUTION

## Daily History
- Nov 20, 2024