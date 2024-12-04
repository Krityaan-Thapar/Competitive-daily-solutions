# Question 

_Difficulty: Moderate_

You are given an array consisting of N integers. You need to find the number of k-element subsequences of the given array where the bitwise AND of the subsequence's elements is maximal. Also, find the maximal AND value.

Example:
Let the array be [1, 3, 6, 7] and K=3. The possible k-element subsequences of the given array are: {1, 3, 6}, {1, 3, 7}, {1, 6, 7}, {3, 6, 7}. Applying AND operation on all possible subsequences we get values: 0, 1, 0, 2 respectively. The maximal AND value of these subsequences is 2, and only 1 subsequence {3, 6, 7} has this value.

**Examples :**
```
Sample Input 1:
2
4 3
1 3 6 7
3 2
9 9 9    

Sample Output 1:
2 1
9 3

Explanation 1:
For the first test case refer to the example explained above.
For the second test case we have, array: [9, 9, 9], N = 3 and K = 2. The possible k-element subsequences of the given array are: {9, 9}, {9, 9}, {9, 9}. Applying AND operation on all possible subsequences we get values: 9, 9, 9 respectively. The maximal AND value of these subsequences is 9, and all subsequences have this value.

Sample Input 2:
2
5 2
1 2 3 4 5
4 4
6 3 7 0

Sample Output 2:
4 1 
0 1
```

**Constraints:**
```
1 <= T <= 10
2 <= N <= 5 * 10^4
2 <= K <= N
0 <= Arr[i] <= 10^8

Where  ‘T’ represents the number of test cases, ‘N’ represents the number of elements present in the array and ‘K’ represents the length of the subsequences.

Time Limit: 1 sec 
```

### Editorial
https://www.naukri.com/code360/problems/maximal-and-subsequences_1115487?leftPanelTabValue=SOLUTION

## Daily History
- Dec 4, 2024