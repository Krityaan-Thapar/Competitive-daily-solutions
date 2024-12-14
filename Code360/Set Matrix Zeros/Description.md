# Question 

_Difficulty: Easy_

You are given an N x M integer matrix. Your task is to modify this matrix in place so that if any cell contains the value 0, then all cells in the same row and column as that cell should also be set to 0.

Requirements:

- If a cell in the matrix has the value 0, set all other cells in that cell's row and column to 0.
- You should perform this modification in place (without using additional matrices).

You must do it in place.

For Example:

If the given grid is this:
[7, 19, 3]
[4, 21, 0]

Then the modified grid will be:
[7, 19, 0]
[0, 0,  0]

**Examples :**
```
Sample Input 1 :
2
2 3
7 19 3
4 21 0
3 3
1 2 3
4 0 6
7 8 9

Sample Output 1 :
7 19 0
0 0 0
1 0 3
0 0 0
7 0 9

Explanation For Sample Input 1 :
For First Case - Similar to the example explained above. 
For Second Case - 
Only the cell (2,2) has zero. So all the elements of the second row and second column are changed to zeros.

Sample Input 2 :
2
4 2
1 0
2 7
3 0
4 8
3 3
0 2 3
1 0 3
1 2 0

Sample Output 2 :
0 0
2 0
0 0
4 0
0 0 0
0 0 0
0 0 0
```

**Constraints:**
```
1 <= T <= 1000
1 <= m, n <= 1000
Sum(m, n) <= 2000000
-2 ^ 31 <= matrix[i][j] <= 2 ^ 31 - 1

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/replace-the-linked-list-with-the-sum-of-nodes-between-0_1380873?leftPanelTabValue=SOLUTION

## Daily History
- Dec 14, 2024