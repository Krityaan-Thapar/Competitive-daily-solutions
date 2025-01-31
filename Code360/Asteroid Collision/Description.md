# Question 

_Difficulty: Moderate_

You are given an array/list 'asteroids' representing asteroids in a row.
For each element of the given array, its absolute value denotes the size of that asteroid, and its sign denotes the direction it moves in(+ve meaning right and -ve meaning left).
An asteroid with a weight of 0 denotes a massless asteroid that moves in the right direction.
All asteroids are moving at the same speed. Whenever two asteroids collide, the smaller asteroid gets destroyed.
If both asteroids are the same size, then both asteroids get destroyed. Two asteroids moving in the same direction never collide.
You are supposed to find the state of the asteroids after all collisions.

Example :
Input: ‘asteroids’ = [3,-2,4]
Output: [3, 4]

Explanation: The first asteroid will destroy the second asteroid. Hence, after the collision, the state of the asteroids will be [3,4].
Note:
You don’t need to print anything. Just implement the given function.

**Examples :**
```
Sample Input 1 :
4
6 7 -9 7

Sample Output 1 :
-9 7

Explanation of Sample Input 1 :
The third asteroid destroys the first and the second asteroids. 
Hence, the remaining asteroids are [-9, 7].

Sample Input 2 :
5
3 4 5 -2 7

Sample Output 2 :
3 4 5 7

Explanation of Sample Input 2 :
The third asteroid destroys the 4th asteroid. 
Hence, the remaining asteroids are [3, 4, 5, 7].
```

**Constraints:**
```
The expected time complexity is O(n).

Constraints :
- 1 <= 'n' <= 10^6
- -10^5 <=asteroids[i] <= 10^5

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/asteroid-collision_977232?leftPanelTabValue=SOLUTION

## Daily History
- Jan 31, 2025