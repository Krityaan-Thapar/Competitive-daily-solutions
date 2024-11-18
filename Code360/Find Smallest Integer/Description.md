# Question 

_Difficulty: Moderate_

You are given an array 'ARR' consisting of 'N' positive numbers and sorted in non-decreasing order, and your task is to find the smallest positive integer value that cannot be represented as a sum of elements of any proper subset of the given array.

An array 'B' is a subset of another array 'A' if each element of 'B' is present in 'A'.
For example:

For the given input array [1, 1, 3],
1 can be represented as the sum of elements of the subset [1],
2 can be represented as the sum of elements of a subset [1, 1],
3 can be represented as the sum of elements of a subset [3],
4 can be represented as the sum of elements of a subset [1, 3],
5 can be represented as the sum of elements of a subset [1, 1, 3]
So, the smallest positive integer value that cannot be represented as a sum of elements of any subset of a given array is 6.

**Examples :**
```
Sample Input 1:
2
4
1 2 3 4
2
1 3

Sample Output 1:
11
2

Explanation of Sample Input 1:
For the first test case, the smallest positive integer value that cannot be represented as a sum of elements of any subset of a given array is 11, as the integer from 1 to 10 can be represented as the sum of elements of any subset of the given array.
For the second test case, the possible values of integers that can be represented as the sum of elements of any subset of the given array are [1, 3, 4], the smallest missing positive integer from which is 2.

Sample Input 2:
2
4
1 1 1 1
6
1 2 6 10 11 15

Sample Output 2:
5
4
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 10^4
0 <= arr[i] <= 10^9
```

### Editorial
https://www.naukri.com/code360/problems/find-smallest-integer_973253?leftPanelTabValue=SOLUTION

## Daily History
- Nov 19, 2024