# Question 

_Difficulty: Hard_

According to Ancient Ninjas, string making is a form of art. There are various methods of string making, one of them uses previously generated strings to make the new one. Suppose you have two strings A and B, to generate a new string C, you can pick a subsequence of characters from A and a subsequence of characters from B and then merge these two subsequences to form the new string.

Though while merging the two subsequences you cannot change the relative order of individual subsequences. What this means is - suppose there are two characters ‘Ai’ and ‘Aj’ in the subsequence chosen from ‘A’, where i < j, then after merging, if i acquires position k and j acquires p then k < p should be true and the same apply for subsequence from B.

Given strings ‘A’, ‘B’, ‘C’ can you count the number of ways to form string ‘C’ from the two strings ‘A’ and ‘B’ by the method described above? Two ways are different if any of the chosen subsequences is different.

As the answer could be large so return it after modulo 10 ^ 9 + 7.
For Example :

let A = a, B = ac, C = ac.

Now In this example, we can take whole string B to form C or take substring {a} and substring {c} from A and B, respectively to make C. Hence the answer is 2.

**Examples :**
```
Sample Input 1:
2
ab
ab
ab
xy
wz
wxzy

Sample Output 1:
4
1

Explanation For Sample Output 1:
For the first test case, 
A = {ab}, B = {}
A = {a}, B = {b}
A = {b}, B = {a}
A = {}, B = {ab}
These are the four possible combinations. Hence the answer is 4.
For the second test case, there is only one way possible i.e. A = {xy}, B = {wz}. Hence the answer is 1.

Sample Input 2:
2
abc
abc
abc
tx
qs
xt

Sample Output 2:
8
0
```

**Constraints:**
```
Constraints :

1 <= T <= 5
1 <= |A|, |B|, |C| <= 100, where |S| represents the length of the String S.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/string-maker_975373?leftPanelTabValue=SOLUTION

## Daily History
- Dec 5, 2024