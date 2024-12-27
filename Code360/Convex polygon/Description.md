# Question 

_Difficulty: Hard_

You are given an array ‘POINTS’ of size ‘N’. Each element of ‘POINTS’ contains two integers, ‘[X, Y]’ representing a point on the cartesian plane. These points, when joined sequentially, form a polygon. The task is to find if this polygon is convex (Convex polygon).
Example:

‘POINTS’ = [ [0, 0], [5, 0], [5, 5], [0, 5] ], ‘N’ = 4.
As the given polygon is a convex polygon, you should return ‘True’ as the answer.

Note:
1. The polygon formed by the given points is always a Simple polygon, i.e., exactly two edges intersect at each vertex, and the edges otherwise don’t intersect each other.
2. All the given points are unique.

**Examples :**
```
Sample input 1:
2
6
0 0
10 0
7 5
10 10
0 10
2 5
5
-10 5
-10 10
-5 15
0 15
0 5

Sample output 1:
False
True

Explanation of sample input 1:
Test Case 1:
The interior angle at the vertex ‘(2, 5)’ is more than 180 degrees, so the given polygon is not convex. Thus, you should return ‘False’ as the answer.

Test Case 2:
As the given polygon is a convex polygon, you should return ‘True’ as the answer.

Sample input 2:
2
5
0 0
5 0
5 5
2 8
0 5
5
5 0
15 0
15 10
5 10
10 5 

Sample output 2:
True
False
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 1000
-10^4 <= Value in each element of ‘POINTS’ <= 10^4

Time limit: 1 second
```

### Editorial
https://www.naukri.com/code360/problems/convex-polygon_1466936?leftPanelTabValue=SOLUTION

## Daily History
- Dec 27, 2024