# Question 

_Difficulty: Moderate_

You are given two integers 'n' and 'm', the dimensions of a grid. The coordinates are from (0, 0) to (n - 1, m - 1). The grid can only have values 0 and 1. The value is 0 if there is water and 1 if there is land. 

An island is a group of ‘1’s such that every ‘1’ has at least another ‘1’ sharing a common edge.

You are given an array 'queries' of size 'q'. Each element in 'queries' contains two integers 'x' and 'y', referring to the coordinates in the grid.

Initially, the grid is filled with 0, which means only water and no land. At each query, the value of 'grid' at (x, y) becomes 1, which means it becomes land. Find out, after each query, the number of islands in the grid.

**Examples :**

```
Sample Input 1:

3 4
3
1 1
1 2
2 3


Sample Output 1:

1 1 2


Explanation of sample input 1 :

Initially, the grid was:
0 0 0 0
0 0 0 0
0 0 0 0

After query (1, 1):
0 0 0 0
0 1 0 0
0 0 0 0
There is one island having land (1, 1).

After query (1, 2):
0 0 0 0
0 1 1 0
0 0 0 0
Since (1, 1) and (1, 2) share a common edge, they form one island. So there is one island having lands (1, 1) and (1, 2).

After query (2, 3):
0 0 0 0
0 1 1 0
0 0 0 1
Now there are two islands, one having lands (1, 1) and (1, 2), and another having land (2, 3).

So the number of islands after each query is [1, 1, 2].


Sample Input 2:

3 5
3
1 1
1 3
1 2


Sample Output 2:

1 2 1
```

**Constraints:**
```
1 <= 'n', 'm' <= 1000
1 <= 'q' <= 10 ^ 4
0 <= 'x' < 'n'
0 <= 'y' < 'm'

All the (x, y) pairs are unique.
```

### Expected Complexities:
Time Complexity: `O(n * m + q)`

### Editorial
https://www.naukri.com/code360/problems/largest-island_840701?leftPanelTabValue=SOLUTION

## Daily History
- Nov 18, 2024