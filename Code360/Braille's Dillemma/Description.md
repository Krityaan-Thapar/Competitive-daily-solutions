# Question 

_Difficulty: Hard_

Abhishek, a blind man has N distinct binary strings all of the equal lengths. A binary string only contains '0's and '1's. The strings are numbered from 1 to N and all are distinct strings. Abhishek can only differentiate between these strings by touching them. In one touch Abhishek can identify one character at a position of any particular string from the set. Your task is to find the minimum number of touches Abhishek has to make so that he finds that all strings are different.

**Examples :**
```
Sample Input 1:
2
3
11100
11101
01100
2
111
000

Sample Output 1:
5
2

Explanation for Sample Input 1:
For the first test case :
There are three strings.
First Abhishkek will touch the last character of all strings.
For the first and third-string Abhishek will identify 0 for the first and third strings and for the second string Abhishek will identify 1. In this way, Abhishek will be able to distinguish the 2nd string.
Next Abhishek will touch 1st character of the 1st and 3rd string. Abhishek will identify 1 for 1st string and 0 for the third string. In this way, Abhishek will distinguish 1st and 3rd strings.
Thus the total number of touches Abhishek make is 5.

For the second test case :
There are two strings.
Abhishek will touch the first character of the first and second string. Abhishek will identify 1 for 1st string and 0 for the second string. In this way, Abhishek will distinguish 1st and 2nd strings.

Sample Input 2:
2
4
10010
11010
01010
01100
3
000101
100010
111000

Sample Output 2:
8
5
```

**Constraints:**
```
1 <= T <= 10
3 <= N <= 10
1 <= k <= 100
Where k  is the length of the string. 
All the strings are distinct.

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/braille-s-dilemma_920550?leftPanelTabValue=SOLUTION

## Daily History
- Dec 26, 2024