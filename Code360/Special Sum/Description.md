# Question 

_Difficulty: Easy_

You are given an array ‘ARR’ of length ‘N’. There are two operations, ‘FIRST_SUM’ and ‘LAST_SUM’ for every index ‘i’ (1 <= i <= N) in the array,

- FIRST_SUM(i) calculates the sum of first i numbers.

- LAST_SUM(i) calculates the sum of last N - i + 1 numbers.

Also for every ‘i’, SPECIAL_SUM(i) can be calculated as:
SPECIAL_SUM(i) = FIRST_SUM(i) + LAST_SUM(i)

Your task is to return the minimum SPECIAL_SUM for 0 <= i <= N - 1.

For example:

Given ‘N’ = 4 and ‘ARR’ = [1, 2, 3, 4].
Then the minimum special sum will be 5 for i = 0 (0-based indexing), which is (1 + 4) = 5.Sum of 1 integer from beginning and end.
For i = 1 it will be (1 + 2) + (3 + 4) = 10
For i = 2 it will be (1 + 2 + 3) + (2 + 3 + 4) = 15
For i = 3 it will be (1 + 2 + 3 + 4) + (1 + 2 + 3 + 4) = 20
All of which are greater than 5. 


**Examples :**
```
Sample Input 1:
2
4
1 2 3 4
4
1 -2 -3 4

Sample Output 1:
5
-5

Explanation of the Sample Input 1:
For the first test case:
The  minimum special sum will be 5 for i = 0 (0-based indexing), which is (1 + 4) = 5.
For i = 1 it will be (1 + 2) + (3 + 4) = 10
For i = 2 it will be (1 + 2 + 3) + (2 + 3 + 4) = 15
For i = 3 it will be (1 + 2 + 3 + 4) + (1 + 2 + 3 + 4) = 20
All of which are greater than 5.  

For the second test case:
The  minimum special sum will be -5 for i = 2 (0-based indexing), which is (1 + (-2) + (-3)) +  (-2 + (-3) + (4)) = -5.
For i = 0 it will be (1) + (4) = 5
For i = 1 it will be (1 + (-2) ) + ( (-3) + 4) = 0 
For i = 3 it will be (1 + (-2) + (-3) + 4)  + (1 + (-2) + (-3) + 4) = 0.
All of which are less than -5.

Sample Input 2:
2
5
1 2 -5 3 1
5 
1 1 1 1 1

Sample Output 2:
-3
2
```

**Constraints:**
```
1 <= T <= 5
1 <= N <= 5 * 1e3
-5 * 1e2 <= arr[i] <= 5 * 1e2
```

### Editorial
https://www.naukri.com/code360/problems/special-sum_1281320?leftPanelTabValue=SOLUTION

## Daily History
- Nov 19, 2024