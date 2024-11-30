# Question 

_Difficulty: Hard_

You are given two sentences, ‘word1’ and ‘word2’, represented as an array of strings of size ‘n’ and ‘m’, respectively. You are also given an array called ‘pairs’. Each element in ‘pairs’ is of the form ‘[u, v]’ where ‘u’ and ‘v’ are strings.

Properties of the array ‘pairs’:

- If ‘[u, v]’ or ‘[v, u]’ is present in ‘pairs’, then the words (or strings) ‘u’ and ‘v’ are identical.
- If ‘u’ and ‘x’ are identical, and ‘v’ and ‘x’ are identical, then the words ‘u’ and ‘v’ are identical.
- Every word is identical to itself, i.e., the word ‘u’ and ‘u’ are always identical.

For two sentences, ‘word1’ and ‘word2’ to be identical:

- For every word (‘word1[i]’) in ‘word1’, the words ‘word1[i]’ and ‘word2[i]’ must be identical.
- ‘word1’ and ‘word2’ must have the same number of words.

Using the array ‘pairs’, you have to determine if ‘word1’ and ‘word2’ are identical.

Example :
‘word1’ = [“exceptional”, “coding”, “skills”]
‘word2’ = [“great”, “coding”, “talent”]
‘pairs’ = [ [“exceptional”, “good”], [“great”, “good”], [“skills”, “talent”] ]

For each word in ‘word1’, we have:
1. “exceptional” = “great”, because “exceptional” = “good” and “good” = “great”
2. “coding” = “coding”, as every word is identical to itself.
3. “skills” = “talent”, because [“skills”, “talent”] is present in ‘pairs’.

As every word in ‘word1’ is identical to the corresponding word in ‘word2’, the given sentences are identical.

Note :
1. The array ‘pairs’ can have words that are not present in ‘word1’ and ‘word2’.
2. Each pair ‘[u, v]’ in ‘pairs’ is unique, and if a pair ‘[u, v]’ is present, then there will never be a pair ‘[v, u]’.
3. You do not need to print anything; it has already been taken care of. Just implement the function.

**Examples :**

```
Sample Input 1 :
2
11246
81

Sample Output 1 :
True
False

Explanation Of Sample Input 1 :
Test Case 1:
So according to this test case string given is ‘11246’ so in this string possible substring is ‘1’, ‘1’, ‘2’, ‘4’, ‘6’, ‘11’, ‘12’, ‘24’, ‘46’, ‘112’, ‘124’, ‘246’, ‘1124’, ‘1246’, ‘11246’ so we return ‘True’ as there are substrings like ‘2’, ‘6’, ‘12’ and so on which can be defined in the form of the product of two consecutive integers like we can write :
‘2’as ‘2*1’
‘6’as ‘3*2’
‘12’as ‘4*3’

Test Case 2:
So according to this test case string given is ‘81’ so in this string possible substrings are ‘8’, ‘1’, ‘81’ so we return ‘False’as for any substring we can’t define in the form of the product of two consecutive integers.

Sample Input 2 :
2
636
75

Sample Output 2 :
True
False
```

**Constraints:**
```
1 <= T <= 1
1 <= n, m <= 1000
0 <= p <= 2000
Each element of ‘pairs’ contains exactly two words.
Length of each word in ‘word1’, ‘word2’ and ‘pairs[i]’ is in the range [1, 20].
Value of each word in ‘word1’, ‘word2’ and ‘pairs[i]’ varies from [a, z].

Where ‘T’ is the number of test cases, ‘n’ is the number of words in ‘word1’, ‘m’ is the number of words in ‘word2’, and ‘p’ is the number of elements in ‘pairs’.

Time limit: 1 second
```

### Editorial
https://www.naukri.com/code360/problems/identical-sentences_1381853?leftPanelTabValue=SOLUTION

## Daily History
- Nov 30, 2024