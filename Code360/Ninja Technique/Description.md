# Question 

_Difficulty: Moderate_

Ninja has its own technique of making a decision to do something or not. This technique is known as the ninja technique. In this technique, Ninja generates a random string containing only digits, and if any substring whose integer value can be defined as the product of two consecutive integers i.e ‘X = N*(N+1)’ then Ninja do that work else didn’t. So now Ninja wants to invest in the stock market so he is using his ninja technique for deciding.

So your task is to write a code that can check whether the string contains any substring whose integer value can be defined as the product of two consecutive integers. If any substring exists you should return ‘True’else return‘False’.

Note :

Substring with integer value ‘0’is not considered as special and check only for integers up to length ‘9’as beyond ‘9’integer can’t hold values.

Example :

For the string ‘1242’ we return ‘True’ as for substring:
‘12’ we can be defined as the product of two consecutive integers i.e ‘3’ and ‘4’.
‘2’ we can be defined as the product of two consecutive integers i.e ‘1’ and ‘2’.
‘42’ can be defined as the product of two consecutive integers i.e ‘6’ and ‘7’.
If the string passes the required condition we have to return ‘True’ else we have to return ‘False’.

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
1 <= T <= 10
1 <= |STR| <= 30
```

### Editorial
https://www.naukri.com/code360/problems/ninja-technique_1263700?leftPanelTabValue=SOLUTION

## Daily History
- Nov 21, 2024