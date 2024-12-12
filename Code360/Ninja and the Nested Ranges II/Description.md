# Question 

_Difficulty: Hard_

Ninja gained confidence while playing with ranges. So, he decided to show off his skills to his crush, Nina. But Nina is hard to impress. She gave him ‘N’ ranges in the form of [Ai, Bi] and asked him to determine for each range how many other ranges it contains and how many other ranges contain it. Ninja finds it challenging to solve the problem and needs your help to impress Nina?

Your task is to return a list of two arrays, ‘RESULT’ where for each range ‘RESULT[ 0 ]’ is an array of size ‘N’ that stores the count of ranges a range contains and ‘RESULT[ 1 ]’ is an array of size ‘N’ that stores the count of ranges a range is contained by.
Note:

Range [X,Y] contains range [A,B] if 'X' <= 'A' and 'Y' >= 'B'.

**Examples :**
```
Sample Input 1:
2
3
3 8
1 3
7 8
4
4 9
9 10
4 10
2 3

Sample Output 1:
1 0 0
0 0 1
0 0 2 0
1 1 0 0

Explanation of Sample Output 1:
Test Case 1 :  
For ‘RESULT[ 0 ]’ array:
Since the range [3, 8] contains only one range: [7, 8], the output corresponding to [3, 8] is 1.
The range [1, 3] does not contain any of the ranges. Therefore, the output corresponding to [1, 3] is 0.
The range [7, 8] does not contain any of the ranges. Therefore, the output corresponding to [7, 8] is 0.

For ‘RESULT[ 1 ]’ array:
The range [3, 8] is not contained by any of the ranges. Therefore, the output corresponding to [3, 8] is 0.
The range [1, 3] is not contained by any of the ranges. Therefore, the output corresponding to [1, 3] is 0.
Since the range [7, 8] is contained by only one range: [3, 8], the output corresponding to [7, 8] is 1.

Test Case 2 :     
For ‘RESULT[ 0 ]’ array:
The range [4, 9] does not contain any of the ranges. Therefore, the output corresponding to [4, 9] is 0.
The range [9, 10] does not contain any of the ranges. Therefore, the output corresponding to [9, 10] is 0.
Since the range [4, 10] contains two ranges: [4, 9] and [9, 10], the output corresponding to [4, 10] is 2.
The range [2, 3] does not contain any of the ranges. Therefore, the output corresponding to [2, 3] is 0.

For ‘RESULT[ 1 ]’ array:
Since the range [4, 9] is contained by only one rang:e [4, 10], the output corresponding to [4, 9] is 1.
Since the range [9, 10] is contained by only one range: [4, 10], the output corresponding to [9, 10] is 1.
The range [4, 10] is not contained by any of the ranges. Therefore, the output corresponding to [4, 10] is 0.
The range [2, 3] is not contained by any of the ranges. Therefore, the output corresponding to [2, 3] is 0.

Sample Input 2:
2
5
5 8
8 11
5 13
13 14
3 15
4
22 91
25 40
66 85
57 83

Sample Output 2:
0 0 2 0 4
2 2 1 1 0
3 0 0 0
0 1 1 1
```

**Constraints:**
```
1 <= T <= 5
1 <=  N <= 2000
1 <= Ai < Bi <= 10 ^ 6

All ranges are distinct.

Where ‘T’ is the number of test cases, ‘N’ is the number of ranges in the array, ‘RANGES’ and ‘Ai’ and ‘Bi’ are the integers representing the ‘i’th range: [Ai, Bi] in array ‘RANGES’.

Time limit: 1 second.
```

### Editorial
https://www.naukri.com/code360/problems/ninja-and-the-nested-ranges-ii_1467998?leftPanelTabValue=SOLUTION

## Daily History
- Dec 13, 2024