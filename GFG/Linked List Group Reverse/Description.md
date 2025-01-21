# Question 

_Difficulty: Medium_

Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

**Examples :**
```
Input: head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.
```

**Constraints:**
```
1 <= size of linked list <= 10^5
1 <= data of nodes <= 10^6
1 <= k <= size of linked list 
```

**Expected:**
Time: `O(n)`
Space: `O(1)`

### Editorial
https://www.geeksforgeeks.org/reverse-a-linked-list-in-groups-of-given-size-iterative-approach/

## Daily History
- Jan 21, 2025