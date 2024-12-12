# Question 

_Difficulty: Moderate_

Given a linked list containing a series of numbers that are separated by ‘0’. You need to find the sum of the series and replace the series’s elements with its sum.
For Example :

If the given linked list is 3 ->4 ->0 ->5 ->0, you should return linked list as - 7 -> 5.

Note :
You need to replace the sum values in the linked list without using any extra space.
It is guaranteed that there will be no two consecutive zeroes in the linked list.

**Examples :**
```
Sample Input 1 :
2
2 5 7 0 3 4 0 -1
1 2 3 0 -1

Sample Output 1 :
14 7
6

Explanation For Sample Input 1 :
Test Case 1: In the given linked list sum of series 2, 5, 7 is 14, and the sum of series 3,4 is 7. So the modified, linked list will be 14 -> 7.
Test Case 2: The only series formed in the linked list 1,2,3 have sum = 6. Therefore modified linked list will be 6.

Sample Input 2 :
2
5 3 8 2 -1
0 6 0 4 0 -1

Sample Output 2 :
5 3 8 2
6 4
```

**Constraints:**
```
1 <= T <= 50
1 <= N <= 10^5
-10^9 <= data <= 10^9
data ≠ -1.

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/replace-the-linked-list-with-the-sum-of-nodes-between-0_1380873?leftPanelTabValue=SOLUTION

## Daily History
- Dec 12, 2024