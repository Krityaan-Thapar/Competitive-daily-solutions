# Question 

_Difficulty: Moderate_

You have been given a Snake and Ladder Board with 'N' rows and 'N' columns with the numbers written from 1 to (N*N) starting from the bottom left of the board, and alternating direction each row.

For example
For a (6 x 6) board, the numbers are written as follows:
You start from square 1 of the board (which is always in the last row and first column). On each square say 'X', you can throw a dice which can have six outcomes and you have total control over the outcome of dice throw and you want to find out the minimum number of throws required to reach the last cell.
Some of the squares contain Snakes and Ladders, and these are possibilities of a throw at square 'X':
You choose a destination square 'S' with number 'X+1', 'X+2', 'X+3', 'X+4', 'X+5', or 'X+6', provided this number is <= N*N.
If 'S' has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row 'i' and column 'j' has a "Snake or Ladder" if board[i][j] != -1. The destination of that snake or ladder is board[i][j].

Note :
You can only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving - you have to ignore the snake or ladder present on that square.

For example, if the board is:
-1 1 -1
-1 -1 9
-1 4 -1
Let's say on the first move your destination square is 2  [at row 2, column 1], then you finish your first move at 4 [at row 1, column 2] because you do not continue moving to 9 [at row 0, column 0] by taking the ladder from 4.

A square can also have a Snake or Ladder which will end at the same cell.
For example, if the board is:
-1 3 -1
-1 5 -1
-1 -1 9
Here we can see Snake/Ladder on square 5 [at row 1, column 1] will end on the same square 5.

**Examples :**
```
Sample Input 1 :
3
-1 1 -1
-1 -1 9
-1 4 -1

Sample Output 1 :
1

Explanation to Sample Input 1 :
In the beginning, you start at square 1 [at row 2, column 0]. The optimal path will be:
1. You decided to move to 4 [at row 1, column 2] and must take the ladder to square 9 [at row 0, column 0].
You finished at last cell of the board in 1 dice throw.

Sample Input 2 :
6
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 35 -1 -1 13 -1
-1 -1 -1 -1 -1 -1
-1 15 -1 -1 -1 -1

Sample Output 2 :
4

Explanation to Sample Input 2 :
In the beginning, you start at square 1 [at row 5, column 0]. The optimal path will be:
1. You decide to move to square 2 [at row 5, column 1] and must take the ladder to square 15 [at row 5, column 1].
2. You then decide to move to square 17 [at row 3, column 5] and must take the snake to square 13 [at row 3, column 0].
3. You then decide to move to square 14 [at row 5, column 1] and must take the ladder to square 35 [at row 0, column 1].
4. You then decide to move to square 36 [at row 5, column 1].
You finished at last cell of the board in 4 dice throw.
```

**Constraints:**
```
1 <= N <= 10 ^ 2
1 <= board[i][j] <= N*N or board[i][j] = -1

Where (NxN) is the size of the board.
```

### Editorial
https://www.naukri.com/code360/problems/toggle-k-bits_973006

## Daily History
- Jan 21, 2024