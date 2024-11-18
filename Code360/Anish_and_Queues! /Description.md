# Question 

_Difficulty: Hard_

Anish is very sad due to the poor performance of India in WT20 and thus does not want to complete his data structures homework which says to implement N queues in a single array of length L. The queue number will be given on which the enqueue and dequeue operations will be given and you have to perform the operations on a single array of length L. Can you help him out?
Example:-

Let, 

```
N = 5
L = 10
1 4 1 [ENQUEUE (4 ,1)]
1 3 1 [ENQUEUE (3 ,1)] 
2 1 [DEQUEUE(1)] 
2 2 2 [ENQUEUE(2,2)] 
2 2 [DEQUEUE(2)]
```

Answer:- [0, 0, 4, 0, 2].
The first queue has 4 and 3 so 4 is dequeued out from queue 1 and queue 2 has integer 2 in it, so 2 is dequeued out from queue 2.

**Examples :**
```
Sample Input 1:
1
10 1 5
1 1 1
1 1 3
2 1
2 1
2 1

Sample Output 1:
0
0
1
3
-1 

Explanation for Sample Output 1:
In the first two operations, the answer should be 0 because the enqueue operations are performed successfully. Then for the next two operations, the numbers 1 and 3 are dequeued out and they are printed. In the last operation, -1 is printed because the queue is already empty.

Sample Input 2:
1
10 2 1
2 2 

Sample Output 2:
-1
```

**Constraints:**
```
1 <= T <= 5
1 <= L <= 10^5
1 <= A <= 2
1 <= B <= N
1 <= C <= 10^9 
```

### Editorial
https://www.naukri.com/code360/problems/anish-and-queues_2701763?leftPanelTabValue=SOLUTION

## Daily History
- Nov 18, 2024