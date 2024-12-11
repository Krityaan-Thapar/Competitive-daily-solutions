# Question 

_Difficulty: Hard_

You are given an infinite chessboard (ie: the x-coordinates and y-coordinates can be anything between -infinity to +infinity).
You have a knight placed at coordinates ‘(0, 0)’. Find the minimum number of steps needed to move the knight to ‘(X, Y)’.
The knight has 8 possible moves, each move is two units in a cardinal direction, then one unit in an orthogonal direction.

For example :
As depicted in the photo below, the knight currently at (0, 0) can move to any of the 8 positions: (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2).

Example :
If X = 1 and Y = -1, then we need to find out the minimum number of steps to move the knight from (0, 0) to (1, -1).
We need at least 2 steps to move the knight to the desired position.
First move: (0, 0) -> (2, 1) 
Second move: (2,1) -> (1, -1)
Here we can see that there are many ways, but we need at least 2 steps. Therefore we will return the value 2.

**Examples :**
```
Sample Input 1 :
2
1 1
1 0

Sample Output 1 :
2
3

Explanation For Sample Input 1 :
For test case 1 :
(0, 0)  to (2, -1) to (1,1), therefore 2 steps are required. The other possible way is (0, 0) to (-1, 2) to (1, 1), but we require at least 2 steps to move from (0,0) to (1,-1). 
Hence return value 2.

For test case 2 :
(0, 0) to (2, 1) to (0, 2) to (1, 0), therefore 3 steps are required. 

Sample Input 2 :
2
12 5
5 12

Sample Output 2 :
7
7
```

**Constraints:**
```
1 <= T <= 10      
-100 <= X, Y <= 100

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/minimum-knight-moves_2179628?leftPanelTabValue=SOLUTION

## Daily History
- Dec 11, 2024