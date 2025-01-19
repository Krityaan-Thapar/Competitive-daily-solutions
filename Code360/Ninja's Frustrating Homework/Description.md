# Question 

_Difficulty: Ninja_

Ninja got a summer vacation homework in which he got a booklet containing a very long string and some set of words written in his diary for which he had to search all these words in that string booklet.
His teacher asked him to write all the starting indices for all the words written in the diary after searching that from the string booklet.
Ninja finds this work very frustrating. He tries to find some help from his neighbor and currently, you are the one who is his neighbor.
It is very time consuming to find every word in the string booklet manually. So you decide to design a code for that. Help Ninja!

Note :
Follow 0 based indexing. 
Print the indices in sorted order.

**Examples :**
```
Sample Input 1 :
2
abcab
3
a cab abca
ninjasmart
3
jas art nin 

Sample Output 1:
0 1 2
0 3 7 

Explanation for Sample Input 1:
Test Case 1 :
The given string is “abcab”. The word “a” is present in the string starting from index 0 and ending at index 0, The word “cab” has starting index 2 and ending index 4 , “abca” has starting index 0 ending index 3.

Test Case 2:
The given string is “ninjasmart”. “Jas” has starting index 3 ending index 5, “art” has starting index 8 ending index 10, “nin” has starting index 0 ending index 2.

Sample Input 2:
2
ahishers
4
he she his hers
bheythis
2
hey this 

Sample Output 2:
1 3 4 4
1 4
```

**Constraints:**
```
1 <= T <= 10 
1 <= |S| <= 1000 
1 <= N <= 30 

Where |S| denotes the length of the given string ‘S’. 
```

### Editorial
https://www.naukri.com/code360/problems/ninja-s-frustrating-homework_1823844

## Daily History
- Jan 19, 2024