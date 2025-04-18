# Question 

_Difficulty: Easy_

You are playing a video game, which contains an N x N grid. You start on the top left cell of the grid, and are free to move anywhere through the grid, any number of times.

Each cell in the grid has some number of points that you can collect from it and you can collect points at most once from each cell. Furthermore, it is possible to collect points from a cell, if and only if the cell lies on one of the two diagonals of the grid. Print the maximum number of points you can collect, given the grid.

For example:

If the grid is:
1 2
3 4
We can collect points from all cells as each cell lies on a diagonal. So, the maximum points will be 1+2+3+4 = 10.

**Examples :**
```
Sample Input 1:
2
3 
1 2 3
4 5 6
7 8 9
1
5

Sample Output 1
25
5

Explanation for Sample Input 1:
For test case 1:
    We can sum up all the elements that lie on the diagonals, namely 1+5+9+3+7 = 25.
For Test case 2:
    Since there is only one element, we can take it.    

Sample Input 2:
1
2
4 5
6 7

Sample Output 2:
22
```

**Constraints:**
```
1 <= 'T' <= 10
1 <= ‘N’ <= 1000.
1 <= ‘A[i][j]’ <= 1000, i ∈ [1,N], j ∈ [1,N]
Note: It is guaranteed that the sum of N^2 across all test cases will be at most 10^6.
Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/maximum-points_3744650?leftPanelTabValue=SOLUTION

## Daily History
- Dec 11, 2024
- Jan 15, 2025