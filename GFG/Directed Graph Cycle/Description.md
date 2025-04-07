# Question 

_Difficulty: Medium_

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.

**Examples :**
```
Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 3]]
Output: true
Explanation: 3 -> 3 is a cycle

Input: V = 3, edges[][] = [[0, 1], [1, 2]]
Output: false
Explanation: no cycle in the graph
```

**Constraints:**
```
- 1 ≤ V, E ≤ 10^5
```

**Expected:**
Time: `O(V + E)`
Space: `O(V + E)`

### Editorial
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

## Daily History
- Apr 7, 2025