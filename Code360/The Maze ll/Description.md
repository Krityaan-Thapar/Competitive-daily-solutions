# Question 

_Difficulty: Hard_

Ninja is stuck in a maze with empty spaces and walls. Ninja can go through empty spaces by running up, down, left or right, but he will continue running in the same direction until hitting a wall. When he stops, he could choose the next direction.
Given Ninja's start position, the destination and the maze, find the shortest distance for Ninja to stop at the destination. The distance is defined by the number of empty spaces traveled by Ninja from the start position (excluded) to the destination (included). If Ninja cannot stop at the destination, return -1.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Note :
Both Ninja’s starting cell and the destination cell exist on an empty space, and they will not be at the same position initially.

The given maze does not contain borders (like the red rectangle in the sample pictures), but you could assume the borders of the maze are all walls.

Example :
N = 3, M = 3
Maze = [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 1, 0, 0] ]
Start = [ 0, 0 ]
Destination = [ 2, 1 ]

Explanation : 
Ninja can start from (0,0) and take the right direction and run till (0,2). Then he turns direction to down and runs till (2,2). Then Ninja turns direction to the left and runs till (2,1). 

**Examples :**
```
Sample Input 1 :
1
5 5
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
0 4 
4 4

Sample Output 1 :
12

Explanation Of Sample Input 1 :
For test case 1
The starting position is (0,4) and the destination is (4,4).
One of the shortest ways is : left -> down -> left -> down -> right -> down -> right.
The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
So, we output 12.

Sample Input 2 :
2
3 4
1 0 1 0 
0 0 0 1 
0 0 1 1 
2 1
1 2
3 5
0 0 0 1 0 
0 1 1 1 1 
1 1 0 0 0 
2 4
0 0

Sample Output 2 :
4
-1
```

**Constraints:**
```
1 <= T <= 10
1 <= N <= 100
1 <= M <= 100

Time Limit : 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/maze-runner_3130881

## Daily History
- Jan 17, 2024