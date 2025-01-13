# Question 

_Difficulty: Hard_

Ninja loves to play with strings and anagrams. A palindrome is a string that is read the same backward or forward. An anagram is a string that is formed by rearranging the characters of the string. Ninjas have been given a string ‘STR’, and asked to find the number of substrings whose anagram is palindromic.

**Examples :**
```
Sample Input 1 :
2
aa
abc

Sample Output 1 :
3
3

Explanation For Sample Input 1 :
For first test case :
Substring are: {a, a, aa}
Since, all the substrings are palindromes.
So, the result is 3.

For second test :
Substring are: {a, b, c, ab, bc, abc}
Since, all {a, b, c} are palindromes. And no anagram of {ab, bc, abc} have palindromes. 
So, the result is 3.

Sample Input 2 :
2
aaa
aab

Sample Output 2 :
6
5
```

**Constraints:**
```
1 <= T <= 10
1 <= |STR| <= 5*10^3
The string ‘STR’ contains small letters only.   

Time Limit : 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/palindrome-count_2409873?leftPanelTabValue=SOLUTION

## Daily History
- Jan 13, 2024