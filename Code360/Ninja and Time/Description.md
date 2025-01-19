# Question 

_Difficulty: Hard_

Ninja is sitting for an online examination. He is encountered with a problem with the statement as “For each element in a given array ‘arr’ of integers, find the sum of numbers that have lower index than the current element and are greater than the current number.”

Ninja knows that you are a very good programmer and can help him in solving the problem in a very less amount of time and come up with the most optimized approach to solve the problem. Help Ninja!

**Examples :**
```
Sample Input 1 :
2
8
3 8 5 9 4 7 2 6
4
5 8 4 2

Sample Output 1 :
0 0 8 0 22 17 36 24
0 0 13 17

Explanation for Sample Output 1:
Test case 1:
There is no integer before 3 as it is the first element of the array so the sum of numbers before 3 and greater than 3 is 0.
Sum of numbers before 8 and greater than 8 is 0.
The sum of numbers before 5 and greater than 5 is 8.
The sum of numbers before 9 and greater than 9 is 0.
The sum of numbers before 4 and greater than 4 is 8 + 5 + 9 = 22.
The sum of numbers before 7 and greater than 7 is 8 + 9 = 17.
The sum of numbers before 2 and greater than 2 is 3 + 8 + 5 + 9 + 4 + 7 = 36.
The sum of numbers before 6 and greater than 6 is 8 + 9 + 7 = 24.


Test case 2:
There is no integer before 5 as it is the first element of the array so the sum of numbers before 5 and greater than 5 is 0.
Sum of numbers before 8 and greater than 8 is 0.
Sum of numbers before 4 and greater than 4 is 5 + 8 = 13.
Sum of numbers before 2 and greater than 2 is 5 + 8 + 4 = 17.

Sample Input 2 :
2
3
5 2 10
3
10 2 13

Sample Output 2 :
0 5 0
0 10 0
```

**Constraints:**
```
1 <= T <= 5 
1 <= N <= 10 ^ 4
1 <= arr[i] <= 10 ^ 3

Time Limit: 1 sec.
```

### Editorial
https://www.naukri.com/code360/problems/ninja-is-running-out-of-time_1758496

## Daily History
- Jan 19, 2024