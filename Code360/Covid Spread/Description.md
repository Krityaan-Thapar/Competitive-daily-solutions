# Question 

_Difficulty: Hard_

You are given a city which contains 'N' x 'M' houses, where each house can have one of the following three conditions :

1. The value ‘0’ represents an empty house,
2. The value ‘1’ represents a non-infected person,
3. The value ‘2’ represents an infected person.

It takes one day to propagate the infection from an infected house to its adjacent (Front, Back, Left, Right) non-empty and non-infected house. An empty house can only break the line of propagation of infection.

You need to return the minimum number of days Covid will take to infect each and every house in the city. And for the God’s sake if this is impossible, return -1 instead.

**Examples :**
```
Sample Input 1 :
2
2 2
2 2
0 1
2 3
1 0 1
2 1 0

Sample Output 1 :
1
-1

Explanation to Sample Input 1 :
In the first test case, the minimum number of days Covid will take to infect each and every person in the city is 1, so the output is 1.
In the second test case, Covid cannot be spread to each and every person, so the output is -1.

Sample Input 2 :
2
2 3
1 0 1
2 1 1
3 3
2 1 1
1 1 0
0 1 1

Sample Output 2 :
3
4

Explanation to Sample Input 2 :
In the first test case, the minimum number of days Covid will take to infect each and every person in the city is 3, so the output is 3.
In the second test case, the minimum number of days Covid will take to infect each and every person in the city is 4, so the output is 4.
```

**Constraints:**
```
1 <= 'T' <= 50
1 <= 'N', 'M' <= 100
0 <= 'houses[i][j]' <= 2

Where houses[i][j] denotes the condition of (i,j) house in the city.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/covid-spread_980228?leftPanelTabValue=SOLUTION

## Daily History
- Dec 28, 2024