# Question 

_Difficulty: Hard_

Given a 2D grid having N Rows and M Columns. Each cell of the grid has a character among [ 'U', 'L', 'D', 'R' ] written on it, denoting Up, Left, Down, and Right respectively and indicating the direction in which it is permitted to move from that cell to its neighbor. Your task is to find the minimum number of cells whose direction value is required to be changed so that there exists a path from Top-Left to the Bottom-Right cell by following the directions written on the cells.
For example,

Consider the 2 * 2 grid
R D
R L

Let's call the four cells in the grid as A,B,C,D. In this grid, it is allowed to move from Cell A to Cell B, Cell B to Cell D, Cell C to Cell D and Cell D to Cell C. There are two paths that start from A and ends at D:

1) A->C->D
To follow this path we need to change the value of cell A to “D” and do not need to change the value of cell C. Therefore, the total change for this path is 1.

2) A->B->D
To follow this path we need not to change any of the cell values. Therefore the total changes for this path is 0.

As we can see the minimum changes required to reach the bottom-right cell is Zero therefore the answer is 0 in this case.

**Examples:**
```
Sample Input 1:
2
2 3
DRD
DRL
1 4
RRRR

Sample Output 1:
1
0

Explanation For Sample Input 1:
For the first test case:
We can change the value of the leftmost cell of the bottom row from 'D' to 'R' or we can change the value of the starting cell from 'D' to 'R' to get a path from the Top-Left to 
Bottom-Right cell. Therefore, the minimum direction change required in this case is 1.

For the second test case:
All the cells only allow moving to the right direction. So a path from leftmost to the rightmost cell already exists in this case. Therefore, the answer is 0 in this case.

Sample Input 2:
2 
3 3
DRR
DRR
DRR
1 1
L

Sample Output 2:
1
0
```

**Constraints:**
```
1 <= T <= 10
1 <= N, M <= 100
Each cell of the grid will only have one of ['U', 'L', 'D', 'R'] character.

Time Limit: 1sec
```

### Editorial
https://www.naukri.com/code360/problems/minimum-direction-changes_1069334

## Daily History
- Dec 15, 2024