# Question 

_Difficulty: Hard_

Given a matrix of size ‘N’ x ’M’. Each cell in a grid has a character denoting the next cell that can be visited from the current cell. If 'MATRIX'[i][j] is equal to:

‘U’:- then from (i,j) you can visit (i - 1, j) only if i - 1 >= 0.
‘D’:- then from (i,j) you can visit (i + 1, j) only if i + 1 < n.
‘R’:- then from (i,j) you can visit (i, j + 1) only if j + 1 < m.
‘L’:- then from (i,j) you can visit (i, j - 1) only if j - 1 >= 0.

You can change the direction of each cell at most one time.
You need to determine a minimum number of changes you need to make to reach from the cell (0,0) to the cell('N' - 1, 'M' - 1).

**Examples:**
```
Sample Input 1:
2
3 3
DDD
RRL
UUU
2 2
UU
DD

Sample Output 1:
1
2

Explanation for Sample Output 1:
In test case 1, one of the paths is as follows:
(0,0) --> (1,0) --> (1,1) --> (1,2). Change the direction of (1,2) from ‘L’ to ‘D’. (1,2) -> (2,2).

In test case 2, one of the paths is as follows:
Change the direction of (0,0) cell to ‘R’.
(0,0) --> (0,1).
Change the direction of (0,1) cell from ‘U’ to ‘D’.
(0,1) --> (1,1).
Thus 2 changes are needed to reach (1,1) cell.

Sample Input 2:
2
1 1
D
2 2
RD
RD

Sample Output 2:
0
0

Explanation for Sample Output 2:
In test case 1, there is only one cell and so, we don't need any cell to change its direction. Thus, 0 will be the output.
In test case 2, No changes are required. Thus, 0 will be the output.
```

**Constraints:**
```
1<= T <= 10
1<= N, M <= 100
MATRIX[i][j] = {‘D’,’R’,’U’,’L’}.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/minimum-changes-to-make-valid-path_1266070?leftPanelTabValue=SOLUTION

## Daily History
- Dec 8, 2024