# Question 

_Difficulty: Easy_

Given a sequence of numbers. Find all leaders in sequence. An element is a leader if it is strictly greater than all the elements on its right side.
Note:
1. Rightmost element is always a leader.
2. The order of elements in the return sequence must be the same as the given sequence

Example:
The given sequence is 13, 14, 3, 8, 2 .
13 Not a leader because on the right side 14 is greater than 13.
14 lt is a leader because no one greater element in the right side.
3 Not a leader because on the right side 8 are greater than 3.
8 It is a leader because no one greater element on the right side.
2 It is a leader because it is the rightmost element in a sequence.
Hence there are 3 leaders in the above sequence which are 14, 8, 2.

**Examples :**
```
Sample Input 1:
2
6
6 7 4 2 5 3
4
11 10 9 8

Sample Output 1:
7 5 3
11 10 9 8

Explanation of Sample Output 1:
In test case 1,
6 Not a leader because on the right side 7 is greater than 6.
7 lt is a leader because no one greater element in the right side.
4 Not a leader because on the right side 5 are greater than 4.
2 Not a leader because on the right side 5, 3 are greater than 2.
5 lt is a leader because no one greater element in the right side.
3 It is a leader because it is a rightmost element in a sequence.
Hence there are 3 leaders in sequence 7, 5, 3. 

In test case 2,
Given sequence is in descending order, so all elements are leaders

Sample Input 2:
2
6
5 10 11 12 -1 -2
4
10 -11 -3 -2

Sample Output 2:
12 -1 -2
10 -2

Explanation of Sample Output 2:
In test case 1,
5 Not a leader because on the right side 10 is greater than 5.
10 Not a leader because on the right side 11 is greater than 10.
11 Not a leader because on the right side 12 are greater than 11.
12 lt is a leader because no one greater element in the right side.
-1 lt is a leader because no one greater element in the right side.
-2 It is a leader because it is a rightmost element in a sequence.
Hence there are 3 leaders in sequence 12, -1, -2. 

In test case 2,
10 lt is a leader because no one greater element in the right side.
-11 Not a leader because on the right side -3 are greater than -11.
-3 Not a leader because on the right side -2 are greater than -3.
-2 It is a leader because it is a rightmost element in a sequence.
Hence there are 2 leaders in sequence 10, -2. 
```

**Constraints:**
```
1 <= T <= 50
1 <= N <= 10^4
-10^9 <= ELEMENTS[i] <= 10^9

Where ‘ELEMENTS[i]’ denotes an element at position ‘i’ in the sequence.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/leaders-in-an-array_873144

## Daily History
- Jan 17, 2024