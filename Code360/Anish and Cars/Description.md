# Question 

_Difficulty: Medium_

Anish has brought N cars and organized a race among the cars. The ith car starts in a unique position POSITION[i] and has a unique speed SPEED[i]. Every car starts driving at the same time after the gun is fired and stops at the point of destination D. However, this competition has a unique rule: no car can overtake any other car. Find the number of unique arriving times of the car.
Example:-

Let, 

N = 5
TARGET = 12
POSITION = [10, 8, 0, 5, 3]
SPEED = [2, 4, 1, 1, 3]

Answer:- 3 ( Car 1 and 2 arrive at the same time, car 3 arrives at a different time, car 4 and car 5 arrive at a different time, so there is a total of 3 different arrival times).

**Examples :**
```
Sample Input 1 :
2
1 10
3
3
4 10
4 3 2 1
4 3 2 1

Sample Output 1 :
1
4 

Explanation for Sample Output 1 :
In the first test case, the answer should be 1 because there is only one car and so there is 1 unique arrival time.
In the second test case, the answer should be 4 because every car arrives at a different time.

Sample Input 2 :
1
2 10
6 8 
3 2

Sample Output 2 :
2
```

**Constraints:**
```
1 <= T <= 5
1 <= N <= 10^5
1 <= D <= 10^6
1 <= POSITIONS[i] <= 10^6
1 <= SPEED[i] <= 10^6  

Note:- The positions of the cars are pairwise distinct.

Time Limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/anish-and-cars_2674167?leftPanelTabValue=SOLUTION

## Daily History
- Dec 10, 2024