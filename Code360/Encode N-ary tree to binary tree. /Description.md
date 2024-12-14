# Question 

_Difficulty: Hard_

You have been given an N-ary tree ‘N’ nodes with node ‘1’ as head of the tree. Encode the above N-ary tree into a binary tree such that if only the encoded binary tree was given to you, you could restore the N-ary tree from the encoded binary tree. You also need to write a function that could decode a given binary tree and return a N-ary tree as in input format.
Note:

There is no restriction on how you encode/decode the N-ary tree.

Example:
N-ary Tree is given as follows:-
6
1 -1 2 3 4 -1 5 -1 6 -1 -1 -1 -1
The above N-ary tree and its encoded binary tree can be represented as follows:-
The above binary tree can be represented as follows in their level order traversal:-
1
2 -1
5 3
-1 -1 6 4
-1 -1 -1 -1

**Examples :**
```
Sample Input 1:
2
1 -1 2 3 4 -1 5 -1 6 -1 -1 -1 -1
1 -1 2 3 -1 -1 -1

Sample Output 1:
1 -1 2 3 4 -1 5 -1 6 -1 -1 -1 -1
1 -1 2 3 -1 -1 -1

Explanation for Sample Input 1:
In test case 1,
1 2 -1 5 3 -1 -1 6 4 -1 -1 -1 -1 is the binary tree user will return. Now we will pass this binary tree to be decoded. The decoded N-ary tree will be 1 -1 2 3 4 -1 5 -1 6 -1 -1 -1 -1. It is not necessary to return the same binary tree as above.
Therefore the answer is 1 -1 2 3 4 -1 5 -1 6 -1 -1 -1 -1.
In test case 2,
1 2 -1 -1 3 -1 - is the binary tree encode will return. Now we will pass this binary tree to be decoded. The decoded N-ary tree will be 1 -1 2 3 -1 -1 -1. It is not necessary to return the same binary tree as above.
Therefore the answer is 1 -1 2 3 -1 -1 -1.

Explanation for Sample Input 2:
2
1 -1 2 -1 -1
1 -1 -1

Sample Output 2:
1 -1 2 -1 -1
1 -1 -1 
```

**Constraints:**
```
1 <= T <= 10
1 <= N <= 1000

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/queue-using-stack_799482?leftPanelTabValue=SOLUTION

## Daily History
- Dec 14, 2024