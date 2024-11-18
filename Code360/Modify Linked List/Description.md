# Question 

_Difficulty: Easy_

You are given a linked list containing N nodes where each node is associated with a certain value. Return a linked list as follows: If the input linked list is 1-->2-->3-->4, then the output should be 1-->4-->2-->3. And if the input is 1-->2-->3-->4-->5, then the output should be 1-->5-->2-->4-->3.

In other words, if the original linked list is first -> second -> third -> ……….->thirdlast -> secondlast -> last, then the modified linked list would be first -> last -> second -> second_last -> ...

Note

1. All the node values are positive.

2. The size of the linked list is greater than 1.

3. The end of the linked list is represented by -1.

**Examples :**

```
Sample Input 1:

2
1 2 3 4 -1
1 2 3 4 5 -1

Sample Output 1:

1 4 2 3
1 5 2 4 3

Explanation of Sample Input 1:

Test case 1:
The original Linked List  1 -> 2 -> 3 -> 4 is modified to 1 -> 4 -> 2 -> 3

Test case 2:
The original Linked List  1 -> 2 -> 3 -> 4 ->5 is modified to 1 -> 5 -> 2 ->4 ->3

Sample Input 2:

4
1 2 3 4 5 6 -1
1 -1
1 2 -1 
1 2 3 -1

Sample Output 2:

1 6 2 5 3 4 
1 
1 2 
1 3 2

```

**Constraints:**
```
1 <= T <= 50
1 <= N <= 1e4
```

### Editorial
https://www.naukri.com/code360/problems/modify-linked-list_1095632?leftPanelTabValue=SOLUTION

## Daily History
- Nov 18, 2024