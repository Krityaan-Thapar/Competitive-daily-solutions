# Question 

_Difficulty: Moderate_

Alice and Bob recently studied bitwise operators and were extremely fascinated by them. Alice found the following function in a book :
Function magic(P, Q):
while Q > 0 :
A = P AND Q
B = P XOR Q
Q = A * 2
P = B
return P

Alice wondered how many times the while loop would run for any value of ‘P’ and ‘Q’. Alice gave Bob the binary representation of ‘P’ and ‘Q’ and asked him to help her count this.
Help Bob count the number of times the while loop would run for the given value of ‘P’ and ‘Q’.


**Examples :**
```
Sample Input 1:
2 
110
10
1
1

Sample Output 1:
3
2

Explanation for Sample Input 1:
In the first test case, initially ‘P’ is 6 and ‘Q’ is 2. After the first iteration, ‘P’ becomes 4 and ‘Q’ becomes 4. After the second iteration, ‘P’ becomes 0 and ‘Q’ becomes 8. After the third iteration, ‘P’ becomes 8 and ‘Q’ becomes 0.
In the second test case, initially ‘P’ is 1 and ‘Q’ is 1. After the first iteration, ‘P’ becomes 0 and ‘Q’ becomes 2. After the second iteration ‘P’ becomes 2 and ‘Q’ becomes 0.

Sample Input 2:
2
1101
101
111
11101

Sample Output 2:
3
4
```

**Constraints:**
```
1 <= T <= 10
1 <= |P|, |Q| <= 10^5
Sum of all |P| + |Q| overall test cases will not exceed 10^6. 

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/count-the-loop_3125931

## Daily History
- Jan 19, 2024