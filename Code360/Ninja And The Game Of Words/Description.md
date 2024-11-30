# Question 

_Difficulty: Moderate_

Ninja and his friend playing a game in which his friend gave him a string ‘STR’ that can contain spaces and a List/Array ‘WORDS’ which is of type string containing ‘N’ strings of words. Ninja’s task is to count the occurrences of all the words in ‘STR’.

For Example:
‘STR’ = “i am a Ninja”, ‘N’ = 3 and ‘WORDS[]’ = [“Ninja”,”a”,”am”]. Then the output should be [1,1,1]. Because the occurrence of “Ninja” in ‘STR’ is 1 and the occurrence of “a” in ‘STR’ is 1.Similarly occurrence of “am” is 1.

Note:
The output should be in the same order as given in ‘WORDS’.
Can you help Ninja to generate all valid strings from ‘STR’ by minimum removals?

**Examples :**
```
Sample Input 1:
2
2
Hi i am ninja and i love coding
ninja
m  
5
Hey ninja ! How are you ?
Hey  
ninja
Ninja 
How 
yo

Sample Output 1:
1 0
1 1 0 1 0

Explanation for Sample Output 1:
For the first test case : 
1. There is only one occurrence of “ninja” in ‘STR’= “Hi i am ninja and i love coding”.
2. There is no occurrence of “m” in ‘STR’ = “Hi i am ninja and i love coding”.

For the second test case:
1. There is 1 occurrence of “Hey” in given ‘STR’ = “Hey ninja ! How are you ?”
2. There is 1 occurrence of “ninja” in given ‘STR’ = “Hey ninja ! How are you ?”
3. There is 0 occurrence of “Ninja” in given ‘STR’ = “Hey ninja ! How are you ?”
4. There is 1 occurrence of “How” in given ‘STR’ = “Hey ninja ! How are you ?”
5. There are 0 occurrences of “yo” in given ‘STR’ = “Hey ninja ! How are you ?”

Sample Input 2:
2
2
the Ninja always wins the game of coding
nja 
the
3
Hey There I am enjoying algorithms
HEY
A
There

Sample Output 2:
0 2 
2 0 1

Explanation for Sample Output 2:
For the first test case : 
1. There is no occurrence of “nja” in ‘STR’= “the Ninja always wins the game of coding”.
2. There is 2 occurrences of “the” in ‘STR’ = “the Ninja always wins the game of coding”.

For the second test case:
1. There are 2 occurrences of “Hey” in given ‘STR’ = “Hey There I am enjoying algorithms”
2.There are 0 occurrences of “A” in given ‘STR’ = “Hey There I am enjoying algorithms”
3. There is 1 occurrence of “There” in given ‘STR’ = “Hey There I am enjoying algorithms”
```

**Constraints:**
```
1 <= ‘T’ <= 100
1 <= |STR| <= 4000
1<= N <= 4000
1<= |WORDS[i]| <= 4000

Where  |'STR'| denotes the length of the given string and ‘|WORDS[i]|’ denotes the length of the string word.  
```

### Editorial
https://www.naukri.com/code360/problems/ninja-and-the-game-of-words_1214642?leftPanelTabValue=SOLUTION

## Daily History
- Dec 1, 2024