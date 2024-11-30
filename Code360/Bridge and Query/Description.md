# Question 

_Difficulty: Hard_

You are given a connected, unweighted and undirected graph with ‘N’ nodes [0 to N - 1] and ‘M’ edges. Your task is to answer ‘Q’ queries on this graph. Each query consists of four integers ‘A’, ‘B’, ‘C’, and ‘D’. For the current query add an edge between nodes numbered ‘A’ and ‘B’ (note that this operation is temporary and only for the current query). Now, output the maximum number of bridge edges occurring on any path between ‘C’ and ‘D’.

Note: An edge between node ‘u’ and ‘v’ is said to be a bridge edge, if after removal of an edge ‘u’ - ‘v’, there is no path between node ‘u’ and ‘v’.

For example:
For given N = 4, M = 3, Q = 1, A = 2, B = 3, C = 0 and D = 3
For all queries, we are temporarily adding an edge between nodes, and here, after the addition of an edge 2 - 3,  the graph looks like this, So, the number of bridge edges on the path from node 0 to 3 is 1 i.e 0 - 1.

**Examples :**
```
Sample Input 1:
4 3 2
0 1
1 2
1 3
2 3 0 3
2 3 2 3

Sample Output 1:
1
0

Explanation of Sample Output1:
In the first query, after the addition of an edge 2 - 3,  the graph looks like this:So, the number of bridge edges on the path from node 0 to 3 is 1 i.e 0 - 1.
In the second query, there is no bridge edge in the above graph after adding edges 2-3. So the number of bridge edges is equal to 0.
Note: For each query, we are temporarily adding an edge between nodes.

Sample Input 2:
6 5 1
0 1
1 2
1 3
3 4
4 5
0 4 2 5

Sample Output 2:
2

Explanation of Sample Output 2:
In the first query, after the addition of an edge 0 - 4  the graph looks like this:
So, the number of bridge edges are 2 i.e( 2 - 1 and 4 - 5)
```

**Constraints:**
```
1 <= Q <= 100
1 <= N, M <= 100
0 <= u, v <= N - 1
0 <= A, B, C, D < N - 1

Time Limit: 1 sec.
```

### Editorial
https://www.naukri.com/code360/problems/bridge-and-query_1796210?leftPanelTabValue=SOLUTION

## Daily History
- Dec 1, 2024