# Question 

_Difficulty: Ninja_

You are given an array of the strings “words” of size 'M' and another string “result”. You have to treat it as an equation in which the left side is represented by the array “words” and the right side is represented by the string "result". Your task is to determine whether the equation is solvable or not under the following conditions:

1. Each character is decoded as a digit in the range [0, 9].
2. Each character must have only one mapping, and every pair of characters must map to different digits.
3. Each element of the array “words” and the string “result” are decoded as one number without the leading zeros.
4. The sum of the numbers on the left-hand side (words) must equal the number on the right-hand side (result).

Note:

1. The array “words”, and the string “result” contain only the uppercase English letters.
2. The number of different characters used in the expression is at most 10.


**Examples:**
```
Sample Input 1:
1
2
SEND MORE
MONEY

Sample Output 1:
true

Explanation Of Sample Input 1:
We can map ‘S’ -> 9, ‘E’ -> 5, ‘N’ -> 6, ‘D’ -> 7, ‘M’ -> 1, ‘O’ -> 0, ‘R’ -> 8, ‘Y’ -> 2. So, “SEND” will decode as 9567, “MORE” as 1085, and “MONEY” as 10652. Also the equation SEND + MORE = MONEY, 9567 + 1085 = 10652 will satisfy. 

Sample Input 2:
1
2
LEFT CODE
CODED

Sample Output 2:
false

Explanation Of Sample Input 2:
There is no mapping available that can satisfy the required equation.
```

**Constraints:**
```
1 <= T <= 100
2 <= M <= 5
1 <= |WORDS[i]|, |RESULT| <= 7

The number of different characters used in the expression is at most 10.

Time Limit: 1sec
```

### Editorial
https://www.naukri.com/code360/problems/verbal-arithmetic-puzzle_1235235?leftPanelTabValue=SOLUTION

## Daily History
- Dec 15, 2024