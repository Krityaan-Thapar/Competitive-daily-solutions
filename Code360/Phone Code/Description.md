# Question 

_Difficulty: Hard_

One day ninja saw his father using an old phone with a number pad and thought of a scenario. She saw that the phone had a numeric keypad and each number was mapped to some alphabets as shown in the figure below. She has a list of valid words. She wants to create an algorithm that would take a given sequence of numbers as input and return a list of matching words that are also present in her list of valid words.

Note:
You can convert the list of valid words into any data structure you desire.

For example :
If the sequence of number = 2633, and the list of valid words = [ride, used, code, tree, boed], 
Then you would print “code” and “boed” as they can be formed by using the digit sequence and they are also present in the list of valid words.

**Examples :**
```
Sample Input 1:
1
2633 
5
used code ride tree boed

Sample Output 1:
code
boed

Explanation of sample input 1:
In the first test case, 
The words that can be formed by using the digit sequence and that are also present in the list of valid words are: “code and boed

Sample Input 2:
2
22 
6
ab ac mn op bc ws
234 
6
bcd cde efg bdg cfh aei

Sample Output 2:
ab 
ac
bc 
bdg 
cfh 
aei

Explanation of sample input 1:
In the first test case, 
The words that can be formed by using the digit sequence and that are also present in the list of valid words are: ab, ca, and bc.
In the second test case, 
The words that can be formed by using the digit sequence and that are also present in the list of valid words are: bdg, cfh, and aei.
```

**Constraints:**
```
1 <= T <= 10
1 <= Sequence <= 10
1 <= W <= 200

where ‘T’ is the number of test cases, “sequence” is the length of the given sequence of numbers, and “W”, is the number of valid words each test case can have. 

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/phone-code_1230549?leftPanelTabValue=SOLUTION

## Daily History
- Dec 16, 2024