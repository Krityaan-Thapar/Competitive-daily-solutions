# Question 

_Difficulty: Moderate_

You are given three positive integers ‘A’, ‘B’, and ‘M’. Your task is to find out the result of ‘A^B’ mod ‘M’.

This task was too easy for Ninja, and being a top-class ninja, he likes to make things a little difficult in order to enjoy solving them. So he converted B into base 3 and is now trying to find the answer.

But it seems like he made the task a little too difficult for himself. Being a good friend of Ninja, can you help find him ‘A^B mod M’ when ‘A’, ‘M’ is given in base 10 and ‘B’ is in base 3?


**Examples :**
```
Sample Input 1 :
1
2 11 6

Sample Output 1 :
4

Explanation for sample input 1 :
‘B’ is ‘10’ in base 3 which is equal to 4 in base 10. Hence the answer is 2^4 mod 6 which is equal to 4.

Sample Input 2 :
2
5 201 7
6 120 9

Sample Output 2 :
5
0

Explanation for sample input 2 :
For test case 1, ‘B’ equals 19 in base 10. 5^19 mod 7 = 5.
For test case 1, ‘B’ equals 15 in base 10. 6^15 mod 9 = 0.
```

**Constraints:**
```
1 <= T <= 10 
1 <= A <= 10^6 
1 <= M <= 10^6 
1 <= |B| <= 250 
Where |B| is the number of digits of ‘B’ in base 3. 

Time Limit: 1 sec 
```

### Editorial
https://www.naukri.com/code360/problems/cubic-square_1470713?leftPanelTabValue=SOLUTION

## Daily History
- Jan 15, 2025