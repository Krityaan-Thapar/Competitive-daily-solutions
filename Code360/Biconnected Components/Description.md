# Question 

_Difficulty: Hard_

You are given an undirected graph of N nodes and M edges. You are required to find out the number of bi-connected components of the graph. We donot count an isolated vertex as a biconnected component

**Examples :**
```
Sample Input 1:
2
7 8
1 2
1 3 
1 4 
1 5
2 6
2 7
4 5 
7 6
3 2
1 2 
1 3

Sample Output 1:
4
2

Explanation For Sample Output 1:
In the above graph, the different biconnected components are:
2-7, 6-7, 2-6
1-3
1-2
1-4, 4-5, 1-5

For test case 2 the graph looks as above. It has 2 biconnected components
1 - 2
1 - 3

Sample Input 2:
3
3 3
1 3
1 2
2 3
4 4
1 3
1 2
2 3
3 4
1 0

Sample Output 2:
1
2
0

Explanation For Sample Output 2:
In test case 3 since there is only 1 isolated vertex, we output 0.
```

**Constraints:**
```
1 <= T <= 10
1 <= N, M <= 10^4
1 <= u, v <= N
```

### Editorial
https://www.naukri.com/code360/problems/number-of-biconnected-components_1805969?leftPanelTabValue=PROBLEM

## Daily History
- Nov 19, 2024