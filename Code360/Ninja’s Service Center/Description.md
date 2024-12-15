# Question 

_Difficulty: Moderate_

Ninja wants to start a service center in town. But people being quite lazy these days, he decided to open the service center in such a place that the sum of the euclidian distance of his service center from all his customer’s location is minimum. Ninja has positions of all its customer in a 2D map, but Ninja doesn’t know how to minimize the euclidian distance. Being his business advisor your task is to help Ninja find a suitable position for his service center.

Given a 2-D array ‘location’ where locations[ i ][ 0 ] and location[ i ][ 1 ] denotes the x and y coordinates of position of ‘i-th’ person.You need to return the minimum sum of Euclidian distance of Ninja’s service center from all customers.

The euclidian distance of a point [ x2, y2 ] from [ x1,y1 ] is given as sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

Note :
You need to round up your answer to the nearest three decimal places.

For Example :
If the position of the customers is [ [ 1,0 ], [ 4,0 ], [ 6,0 ] ], then if Ninja opens his service center at [ 4,0 ] then he will get the minimum sum of euclidian distance = 5.000  from all customers.

**Examples :**
```
Sample Input 1 :
2
3
2 0
0 0
1 1
1
3 4

Sample Output 1 :
2.733
0.000

Explanation Of Sample Input 1 :
Test Case 1: If NInja opens his service center at [ 1,0 ] then he will get a sum of euclidian distances = 3. But if he opens his center at [ 1, 0.5773 ] then he will get a minimum sum of distances = 2.73205. Round to the nearest three decimal places = 2.733
Test Case 2: There is only one customer so the minimum distance can be ‘0’.

Sample Input 2 :
2
3
2 2
3 4
4 1
2
5 3
3 2

Sample Output 2 :
4.320
2.237
```

**Constraints:**
```
1 <= T <= 10
1 <= N <= 10^3
0 <= location[ i ][ 0 ], location[ i ][ 1 ] <= 10^3

Where  location[ i ][ 0 ], location[ i ][ 1 ] denotes the ‘ x ’ and ‘ y ’ coordinates of the position of customers.

Time Limit : 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/ninja-s-service-center_1376426?leftPanelTabValue=SOLUTION

## Daily History
- Dec 16, 2024