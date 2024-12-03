# Question 

_Difficulty: Easy_

You are given an array 'ARR' of 'N' integers and a non-negative integer 'K'. Your task is to find if there exists two indices 'i' and 'j' such that ARR[i]-ARR[j] = K, given 'i' is not equal to 'j'. If there exist such indices you have to return TRUE else you have to return FALSE. According to the return value, ‘YES’ or ‘NO’ will be printed, ‘YES’ for TRUE and ‘NO’ for FALSE.

For example :
1. ARR = [5,3,7,1] and K=2
We can see for i=1 and j =2, ARR[i]-ARR[j] = 2 .
So we will return TRUE.
2. ARR = [-2,7,3,1,5] and K=10
We can see for any two indices it is not possible that the difference in their value is equal to K.
So we will return FALSE.

**Examples :**
```
Sample input 1:
4
5 3
4 3 2 1 5
3 7
6 1 3 
7 12
-3 5 -2 4 1 0 9
5 2
12 22 1 2 8

Sample output 1:
YES
NO
YES
NO

Explanation for sample output 1
(i) The possible indices are i=1 and j=4.
(ii) There do not exist 2 indices that satisfy the criteria.
(iii) The possible indices are i=7 and j=1.
(iv) There do not exist 2 indices that satisfy the criteria.

Sample input 2:
3
4 1
2 4 6 8 
5 0
5 4 5 3 1
7 10
-10 2 5 3 2 1 0

Sample output 2:
NO
YES
YES

Explanation for sample output 2:
(i) There do not exist 2 indices that satisfy the criteria.
(ii) The possible indices are i=1 and j=3.
(iii) The possible indices are i=7 and j=1.
```

**Constraints:**
```
1<= T <=100
1 <= N <= 10^5
-10^5 <= ARR[i] <= 10^5

Where 'T' denotes the number of test cases, 'N' denotes the number of elements in the array ‘ARR’ respectively, and 'ARR[i]' denotes the 'i-th' element of the array 'ARR'. 
```

### Editorial
https://www.naukri.com/code360/problems/check-difference_1090493?leftPanelTabValue=SOLUTION

## Daily History
- Dec 3, 2024