# Question 

_Difficulty: Hard_

You have been given a number ‘NUM’. Your task is to count total structurally unique binary search trees from keys 1 to ‘NUM’ considering we should use each key from 1 to ‘NUM’ only once.

Two binary search trees are different if there is at least one node during traversal which is different in values or present in one tree but not present in another tree.
Note:

The answer can be large, hence the return answer % ‘MOD’, where ‘MOD’ is a large prime number (10^9 + 7).

**Examples :**
```
Sample Input 1:
2
2
1

Sample Output 1:
2
1

Explanation of sample input 1:
In the first test case, 2 unique BST are possible.
In the second test case, only 1 tree is possible.

Sample Input 2:
2
3
4

Sample Output 2:
5
14

Explanation of sample input 2:
In the first test case, 5 unique BST are possible.
In the second test case, similar to the above way, 14 unique BST are possible.
```

**Constraints:**
```
- 1 <= T <= 100   
- 1 <= NUM <= 500

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/construct-bsts_920468

## Daily History
- Jan 28, 2025