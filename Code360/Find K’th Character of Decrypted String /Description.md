# Question 

_Difficulty: Moderate_

You have been given an Encrypted String where repetitions of substrings are represented as substring followed by the count of substrings.

Example: String "aabbbcdcdcd" will be encrypted as "a2b3cd3".

You need to find the 'K'th character of Decrypted String. Decrypted String would have 1-based indexing.

Note :
- Input string will always be lowercase characters without any spaces.
- If the count of a substring is 1 then also it will be followed by Integer '1'. Example: "aabcdee" will be Encrypted as "a2bcd1e2". This means it's guaranteed that each substring is followed by some Integer.
- Also, the frequency of encrypted substring can be of more than one digit. For example, in "ab12c3", ab is repeated 12 times. No leading 0 is present in the frequency of substring.
- The frequency of a repeated substring can also be in parts.
Example: "aaaabbbb" can also have "a2a2b3b1" as Encrypted String.

**Examples :**
```
Sample Input 1 :
a2b3cd3
8

Sample Output 1 :
c

Explanation to Sample Input 1 :
S = "a2b3cd3"
Decrypted String of S = "aabbbcdcdcd"
According to 1-based indexing for S, the 8th character is 'c'.

Sample Input 2 :
ab12c3
20

Sample Output 2 :
b

Explanation to Sample Input 2 :
S = "ab12c3"
Decrypted String of S = "ababababababababababababccc"
So 20th character is 'b'.
```

**Constraints:**
```
2 <= N <= 10^5 
1 <= K <= M 
1 <= M <= 10^18 

Where 'N' is the length of String 'S' and 'M' is the length of the Decrypted String of 'S'. All the characters of String 'S' are lowercase English letters. 
Time Limit: 1sec 
```

### Editorial
https://www.naukri.com/code360/problems/find-k-th-character-of-decrypted-string_630508?leftPanelTabValue=SOLUTION

## Daily History
- Jan 13, 2024