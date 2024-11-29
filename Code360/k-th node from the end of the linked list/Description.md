# Question 

_Difficulty: Easy_

Given the head node of the singly linked list and an integer ‘k’, , find the value at the kth node from the end of the linked list.
For example:
51->37->77->12->78
For the above-linked list, if k=2, then the value at the kth i.e second node from the end is ‘12’.

**Examples :**
```
Sample Input 1 :
2
43 6 9 1 5 -1
4
3 7 -32 8 11 -1
5

Sample Output 1 :
6
3

Explanation Of Sample Input 1 :
First Test Case : 
The given linked list is: 43->6->9->1->5
We can clearly see that the 4th element from the last is 6 therefore we return a pointer pointing to the element ‘6’.

Second Test Case :
The linked list in this case is 3->7->-32->8->11
The 5th element from last is the first node of the list therefore we return a pointer pointing to the first node i.e. ‘3’

Sample Input 2 :
1
2 26 35 5 -1
1

Sample Output 2 :
5
```

**Constraints:**
```
1 <= T <= 50
0 <= N <= 10^5
-10^9 <= data <= 10^9
1 <=k <=N
node->data ≠ -1.
```

### Editorial
https://www.naukri.com/code360/problems/k-th-node-from-the-end-of-the-linked-list_1171164?leftPanelTabValue=SOLUTION

## Daily History
- Nov 28, 2024