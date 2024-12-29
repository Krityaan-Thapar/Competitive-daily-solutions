# Question 

_Difficulty: Moderate_

Vidit is frequently among the "Wrong-doers" list. To curb his menace, Ms. Manisha, his algorithms teacher, gave him an assignment to keep him busy.

Ms. Manisha coins a term "longest common prefix", which is defined as longest word with which both words start with. For example: the longest common prefix of words: "notify" and "notification" is the word "notif".

Now, Ms. Manisha gives a database of N words to Vidit. Ms. Manisha also gives an algorithm to search a word X in the database. The algorithm is simple and is written as:

1. Compare the word X with each word in the database. We keep on comparing till we find a mismatching letter or end of one of the words is reached.

2. After that it is established either words are equal/unequal or that one is longer than the other.

3. When the algorithm finds the word X in the database, it terminates.

Analysing the algorithm, it shows that the number of steps needed to find a word W is equal to the sum of the lengths of the longest common prefixes of X and each of the words it was compared to.

Vidit comes to you and asks you to write a program that calculates the number of steps the algorithm uses to find each of the Q query words.

**Examples :**
```
Sample Input 1:
8
majmunica
majmun
majka
malina
malinska
malo
maleni
malesnica
3
krampus
malnar
majmun

Sample Output 1:
8
29
14

Explanation:
In the first test case, the number of steps to search for the word "krampus" is 8 because the algorithm only needs to compare its first letter to each word in the database.
When searching for the word "malnar", we need three steps for each of the first three words, and four steps for each of the remaining five words, for a total of 29 steps.
To find the word "majmun" we use a total of 14 steps. For the first word in the database, we have six successful comparisons and one step in which we determine that the word "majmunica" is longer than the query word. For the second word, we also have six successful comparisons and a final step in which it is established that the words are equal. After finding the word, the algorithm terminates with great joy
```

**Constraints:**
```
1 <= N <= 3 * 10^4
1 <= Q <= 3 * 10^4
```

### Editorial
https://www.naukri.com/code360/problems/longest-common-prefix_78332?leftPanelTabValue=SOLUTION

## Daily History
- Nov 29, 2024
- Dec 28, 2024