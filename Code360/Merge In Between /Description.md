# Question 

_Difficulty: Moderate_

You are given two linked lists, ’head1’ and ‘head2’ of size ‘N’ and ‘M’. You are also provided with two integers, ‘X’ and ‘Y’, and your task is to remove the first Linked List’s nodes from index ‘X’ to ‘Y’ and insert all the nodes of the second Linked List in their place.

You need to return the head of the merged Linked List.
For example:

If the first list is: [0 -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL], the second list is: [10 -> 20 -> 30 -> NULL], ‘X’ = 2 and ‘Y’ = 4 then if we remove nodes from index 2 to 4, and after inserting the second list at index 2 then the final list will be: [0 -> 1 -> 10 -> 20 -> 30 -> 5 -> NULL].

**Examples :**
```
Sample Input 1:
2
2 4
0 1 2 3 4 5 -1
10 20 30 -1
3 3
0 1 3 8 11 -1
7 9 -1

Sample Output 1:
0 1 10 20 30 5 -1 
0 1 3 7 9 11 -1

Explanation:
For the first test case, if we remove nodes from index 2 to 4 and after inserting the second list at the index 2 then the final list will be: [0 -> 1 -> 10 -> 20 -> 30 -> 5 -> NULL].
For the second test case, if we remove node at index 3, and after inserting second list at the index 3 then the final list will be: [0 -> 1 -> 3 -> 7 -> 9 -> 11  -> NULL].

Sample Input 2:
2
2 3 
-2 3 5 -7 9 -1
0 0 0 -1
3 4 
3 4 5 2 6 7 -1
9 -1

Sample Output 2:
-2 3 0 0 0 9 -1
3 4 5 9 7 -1
```

**Constraints:**
```
- 1 <= T <= 10
- 3 <= N <= 10 ^ 6
- 1 <= M <= 10 ^ 6
- -10^9 <= Node.Data <= 10^9 and Node.Data != -1
- 1 <= X <= Y < N - 1
- The linked list is 0-indexed.

Time Limit: 1 sec

Note:
You do not need to input or print anything, as it has already been taken care of. Just implement the given function.
```

### Editorial
https://www.naukri.com/code360/problems/merge-in-between_2424967

## Daily History
- Jan 28, 2025