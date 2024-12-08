# Question 

_Difficulty: Hard_

You are given various subsequences of a particular array. You have to return the overall array from these given subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting 0 or more elements without changing the order. For example, for the given array [1, 2, 3, 4, 5], a few valid subsequences are [1, 3, 5], [2, 4], [1, 2, 3, 4, 5].
For Example:

Consider the subsequences = [[1,3,9], [3,9,5]], for the given subsequences the output array could be [1, 3, 9, 5] as: 
1 is before 3 and 9
5 is after 3 and 9
3 is before 9

**Examples :**
```
Sample Input 1:
2
2
1 5 9
1 3 5  
3
5 9
1 3 5
1 5 2

Sample Output 1:
CORRECT
CORRECT

Explanation of Sample Input 1:
For the first test case, subsequences given = [[1, 3, 9], [3, 9, 5]], for the given subsequences the output array could be [1, 3, 9, 5] as: 
1 is before 3 and 9
5 is after 3 and 9
3 is before 9
Hence the answer [1, 3, 9, 5]

For the second test case,  sub sequences given = [[5, 9], [1, 3, 5], [1, 5, 2]], for the given subsequences the output array could be [1, 3, 5, 2, 9] or [1, 3, 5, 9, 2] as: 
9 comes after 5
5 comes after 1 and 3
2 comes after 5 
Hence one of the answer is [1, 3, 5, 2, 9]

Sample Input 2:
1
4
0 1
0 3
1 2
3 2

Sample Output 2:
CORRECT
```

**Constraints:**
```
1 <= T <= 10
1 <= N <= 10^3
1 <= M <= 10^3
0 <= arr[i] <= 10^6

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/printing-array_2410877?leftPanelTabValue=SOLUTION

## Daily History
- Dec 9, 2024