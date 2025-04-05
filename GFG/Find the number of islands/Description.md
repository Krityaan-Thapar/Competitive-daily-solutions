# Question 

_Difficulty: Medium_

Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

**Examples :**
```
Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4

Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2
```

**Constraints:**
```
- 1 ≤ n, m ≤ 500
- grid[i][j] = {'L', 'W'}
```

**Expected:**
Time: `O(n * m)`
Space: `O(n * m)`

### Editorial
https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/

## Daily History
- Apr 5, 2025