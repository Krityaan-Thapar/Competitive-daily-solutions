# Question 

_Difficulty: Easy_

Mr. X runs an internet cafe which has 'K' computers. His internet cafe has 'N' customers who can come anytime throughout the day. Initially, all the 'K' computers are available for customer use. When a customer enters the cafe he first checks whether any available computer is there. If he finds one he starts using it and it is marked unavailable. When he leaves the cafe that computer is again marked as available. If the customer is not able to find any available computer he leaves the cafe immediately.

You are given an integer array ‘ARR’ in which each value occurs exactly 2 times, the index of the first occurrence of any value denotes the arrival time of the customer while the second occurrence denotes the departing time of the customer. Your task is to find the no. of customers who were not able to find any available computer and had to leave the cafe immediately.
For example :

Consider the sequence of customers as [ 1, 2, 3, 2, 3, 1 ] for N = 3 and K = 2.

The procedure takes place as follows :
1) At the start, Customer 1 comes and finds an available computer and starts using it and now the number of available computers is reduced by 1. 

2) Customer 2 comes and he is also able to find an available computer and he starts using the computer. Now all the computers are unavailable.

3) Customer 3 comes and goes back immediately as there are no computers available currently. 

4) Customer 2 leaves the cafe making 1 computer available. 

5) As customer 3 has already left no new computers are made available.

6) Customer 1 leaves the cafe and all the computers are again available. 

As only Customer 3 was unable to find any available computers therefore the answer is 1 for this case.

**Examples:**
```
Sample Input 1:

2
2 2
1 2 2 1
3 2 
1 3 2 1 2 3

Sample Output 1:

0
1

Explanation for Sample Input 1:
For the first test case:
1. Initially, Customer 1 comes and finds an available computer and starts using it. Now only 1 computer is available.
2. Then Customer 2 comes and takes the only available computer. Now all computers are unavailable.
3. Customer 1 leaves the cafe making 1 computer available.
4. Customer 2 leaves the cafe making all the computers available.
As all customers were able to find an available computer and nobody left without using a computer. Hence, the answer is 0 in this case.

For the second test case : 
The procedure takes place as follows :
1. At the start, Customer 1 comes and finds an available computer and starts using it and now the number of available computers is reduced by 1. 
2. Customer 3 comes and he is also able to find an available computer and he starts using the computer. Now all the computers are unavailable.
3. Customer 2 comes and goes back immediately as there are no computers available currently. 
4. Customer 1 leaves the cafe making 1 computer available. 
5. As customer 2 has already left no new computers are made available. 
6. Customer 3 leaves the cafe and all the computers are again available. 
As only Customer 2 was unable to find any available computers therefore the answer is 1 for this case.

Sample Input 2:
2
4 1
1 2 3 4 4 3 2 1
2 2
1 2 1 2

Sample Output 2:
3
0
```

**Constraints:**
```
1 <= T <= 10
1 <= N <= 10^5
1 <= K <= 10^5
1 <= ARR[i] <= N

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/count-customers-who-did-not-get-a-computer_1115775?leftPanelTabValue=SOLUTION

## Daily History
- Dec 15, 2024