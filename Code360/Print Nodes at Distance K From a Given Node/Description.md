# Question 

_Difficulty: Hard_

You are given an arbitrary binary tree, a node of the tree, and an integer 'K'. You need to find all such nodes which have a distance K from the given node and return the list of these nodes.
Distance between two nodes in a binary tree is defined as the number of connections/edges in the path between the two nodes.

Note:

1. A binary tree is a tree in which each node has at most two children. 
2. The given tree will be non-empty.
3. The given tree can have multiple nodes with the same value.
4. If there are no nodes in the tree which are at distance = K from the given node, return an empty list.
5. You can return the list of values of valid nodes in any order. For example if the valid nodes have values 1,2,3, then you can return {1,2,3} or {3,1,2} etc.


**Examples :**
```
Sample Input 1 :

3 5 1 6 2 0 8 -1 -1 7 4 -1 -1 -1 -1 -1 -1 -1 -1
5
2

Sample Output 1 :

7 4 1

Explanation For The Sample Output 1:
Target Node is 5. Nodes at distance 1 from 5 are {6, 2, 3} and nodes at distance 2 are {7, 4, 1}.

Sample Input 2:
7 -1 14 9 -1 13 -1 20 9 -1 8 -1 -1 2 -1 -1 16 -1 -1 
2
6

Sample Output 2:
7
```

**Constraints:**
```
Constraints:
1 <= N <= 3000
0 <= K <= 3000
0 <= nodeValue <= 3000
Where nodeValue donates the value of the node.
Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/print-nodes-at-distance-k-from-a-given-node_842560?leftPanelTabValue=SOLUTION

## Daily History
- Dec 4, 2024