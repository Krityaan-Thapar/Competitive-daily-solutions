# Question 

_Difficulty: Hard_

The King is on a quest to conquer the entire world.
There are ‘N’ kingdoms in the world numbered from 0 to N-1. Each kingdom can only be reached from exactly one of the other kingdoms, except the ‘0th’ kingdom where the King lives. Also, it is possible to reach all other kingdoms from the 0th kingdom.
That is, the world is made up of a network of kingdoms in form of a tree rooted at zero. You are given an array ‘prevKingdom’ denoting that the ith kingdom can only be reached from the ‘prevKingdom[i]th’ kingdom, and prevKingdom[0] = -1.
The King initially lives in the 0th kingdom, but he wants to conquer all other kingdoms; he can only conquer a kingdom if all other kingdoms lying on the shortest path to the 0th kingdom have already been conquered.
Find the number of ways in which the King can conquer the entire world. As this number can be very big, return its modulo 109+7.

Note :
Two ways of conquering the world are considered different if the order in which the king conquered the kingdoms from 1 to N-1 are different. Refer to the example below for a better understanding.

For Example :
If N = 4, prevKingdom = { -1, 0, 0, 1 } , then the network of kingdoms is denoted as:
Then the King has 3 ways to conquer the world:
0 -> 1 -> 2 -> 3
0 -> 1 -> 3 -> 2
0 -> 2 -> 1 -> 3
All these 3 ways satisfy the constraint that before conquering any kingdom all the kingdoms on the shortest path to the 0th kingdom have been conquered, in other words: before conquering kingdom-3 the King must conquer kingdom-1.

**Examples :**
```
Sample Input 1 :
2
4
-1 0 0 1
4
-1 0 1 2 

Sample Output 1 :
3
1

Explanation For Sample Input 1 :
For test case 1 : 
We will return 3, because:
( 0 -> 1 -> 2 -> 3 )
( 0 -> 1 -> 3 -> 2 )
( 0 -> 2 -> 1 -> 3 )
are the only possible ways to conquer the world.

For test case 2 : 
We will return 1, because:
( 0 -> 1 -> 2 -> 3 ) is the only possible way to conquer the world.

Sample Input 2 :
2
8
-1 0 0 1 2 3 3 4
12
-1 0 0 1 2 3 3 4 5 5 6 6

Sample Output 2 :
70
13200
```

**Constraints:**
```
1 <= T <= 10      
0 <= N <= 10000
0 <= prevKingdom[i] < N, and prevKingdom[0] = -1

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/number-of-ways-to-build-empire_2327475?leftPanelTabValue=SOLUTION

## Daily History
- Dec 6, 2024