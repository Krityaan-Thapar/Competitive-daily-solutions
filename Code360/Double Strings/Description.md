# Question 

_Difficulty: Hard_

You are given a string ‘STR’, containing only lowercase English letters.

Your task is to determine the total number of distinct substrings present in ‘STR’ which are double strings.
Note :

1. A double string is a string that is made by concatenation of some string with itself.

2. The length of a double string is at least 2.

For example :

In the string ‘ababab’, there are just two substrings, that are double strings. Both such substrings are ‘abab’, and thus there exists only one distinct substring which is a double string. ‘abab’ can be written as ‘ab’ + ‘ab’. But ‘ababab’ can not be considered as a double string because ‘ab’ has been concatenated twice with itself. 

**Examples :**
```
Sample Input 1 :
1
abcarcar

Sample Output 1 :
1

Explanation for sample input 1 :
In this test case, we can observe that the substring ‘carcar’ can be written as ‘car’ + ‘car’. So, ‘carcar’ is a double substring. Since, this is the only such substring, we print 1.

Sample Input 2 :
1
abbasdasda

Sample Output 2 :
3

Explanation for sample input 2 :
In this case, the substring ‘bb’ can be written as ‘b’ + ‘b’. ‘sdasda’ can be written as ‘sda’ + ‘sda’ and ‘asdasd’ can be written ‘asd’ + ‘asd’. So, a total of 3 substrings exist in the given string which are double strings.
```

**Constraints:**
```
1 <= T <= 5
1 <= |STR| < 2000
Where ‘T’ denotes the number of test cases and |STR| represents the length of the string ‘STR’
```

### Editorial
https://www.naukri.com/code360/problems/double-strings_1461333?leftPanelTabValue=SOLUTION

## Daily History
- Nov 29, 2024