# Question 

_Difficulty: Moderate_

In a chessboard(‘N’ x ‘N’) game of Angles(‘A’) and Demons(‘O’, ‘X’, and ‘Z’), various demons try to kill the angel whose aim is to get across from one end of the board to the opposite end of the board. There are 3 different devils having different powers.

Starting point of Angel can only be on the border but not the corners of the board. He will walk in a straight line(horizontal or vertical only) across the board, one cell every second.

The powers of various devils are as follows:-
OGRE(‘O’): Cannot move but he can kill with his breath. His powers change with time:

In 1st second ‘O’ can kill the angel if the ‘A’ reaches the ogre’s location.
In the 2nd second, ‘O’ can kill if ‘A’ is in 8 surrounding cells.
In 3rd second ‘O’ can kill if ‘A’ reaches the ogre’s location.
In the 4th second, ‘O’ cannot kill ‘A’ in any condition.
This sequence repeats cyclically.

XILL(‘X’): He has the power to kill an angel only if

‘A’ is the same colored cell as ‘X’.
‘X’ is only active at the time equal row number of ‘X’.

ZAHHAK(‘Z’): He leaves a poison trail and moves in the ‘Z’ shape. His first move is ‘down’ and then ‘right’ and keeps on making a trail in that order until he reaches the border. If he reacher a border, he changes his direction of movement to the opposite direction he came from. Angel coming on poison will die immediately.

You need to tell the coordinate of the cell at which the angel will die or output [-1, -1] if Angel successfully crosses the board.
EXAMPLE:

Input: 
'N' = 12
‘A’ = [12 11]
‘O’ = [3, 9]
‘X’ = [8, 4]
‘Z’ = [4, 3]

Output: [5, 11]

The Angel will be killed by the demon(‘X’) at 8th second as follows:

Answer:- [0, 0, 4, 0, 2].
The first queue has 4 and 3 so 4 is dequeued out from queue 1 and queue 2 has integer 2 in it, so 2 is dequeued out from queue 2.

**Examples :**
```
Sample Input 1 :
2
12
12 11
3 9
8 4
4 3
12
12 9
10 2
3 7
2 11

Sample Output 1 :
5 11
-1 -1

Explanation Of Sample Input 1 :
The Angel will be killed by the demon(‘X’) at the 8th second as follows:
The Angel will not be killed by anyone as the demon ‘X’ and angel will be on different color cells at the time of activation of demon ‘X’, and the demon ‘Z’ will not cross paths with the angel during the time of 12 seconds and demon ‘O’ will never reach angel.
The picture depicts the board at ‘T’ = 3.

Sample Input 2:
2
5
4 1
2 4
5 5
1 1
5
4 1
2 4
5 5
4 1

Sample Output 2:
-1 -1
4 1
```

**Constraints:**
```
1 <= 'T' <= 10
5 <= 'N' <= 500
1 <= ‘A[i], A[j]’ <= ‘N’
1 <= ‘O[i], O[j]’ <= ‘N’
1 <= ‘X[i], X[j]’ <= ‘N’
1 <= ‘Z[i], Z[j]’ <= ‘N’
Where ‘i’ and ‘j’ represent the row and column respectively.

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/angles-and-demons_4691848?leftPanelTabValue=SOLUTION

## Daily History
- Dec 6, 2024