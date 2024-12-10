# Question 

_Difficulty: Hard_

You’re given an array 'arr' of size 'n' and an integer 'k'.
Your task is to split 'arr' into 'k' sub-arrays such that the maximum sum achieved from the 'k' subarrays formed must be the minimum possible.
A subarray is a contiguous part of the array.
Return the minimum possible value of the maximum sum obtained after splitting the array into 'k' partitions.

Example:
Input: ‘arr’ = [1, 1, 2] and ‘k’ = 2 
Output: 2

Explanation: If we want to make two subarrays, there are two possibilities: [[1], [1, 2]] and [[1, 1], [2]]. We can see that the maximum sum of any subarray is minimized in the second case. Hence, the answer is 2, which is the maximum sum of any subarray in [[1, 1], [2]].

**Examples :**
```
Sample Input 1:
3 2
1 1 2

Sample Output 1:
2

Explanation of Sample Input 1:
If we want to make two subarrays, there are two possibilities: [[1], [1, 2]] and [[1, 1], [2]]. We can see that the maximum sum of any subarray is minimized in the second case. Hence, the answer is 2, which is the maximum sum of any subarray in [[1, 1], [2]].

Sample Input 2:
4 3
1 2 3 4

Sample Output 2:
4

Explanation of Sample Input 2:
If we want to make three subarrays, there are three possibilities: [[1], [2], [3, 4]], [[1], [2, 3], [4]], and [[1, 2], [3], [4]]. We can see that the maximum sum of any subarray is minimized in the third case. Hence, the answer is 4, which is the maximum sum of any subarray in [[1, 2], [3], [4]].
```

**Constraints:**
```
1 <= 'n' <= 10^4
1 <= 'k' <= N
1 <= 'arr[i]' <= 10^4

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/split-the-given-array-into-k-sub-arrays_1215015?leftPanelTabValue=SOLUTION

## Daily History
- Dec 10, 2024