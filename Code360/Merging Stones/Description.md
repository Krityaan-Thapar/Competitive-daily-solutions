# Question 

_Difficulty: Ninja_

You are given an array of piles of stones ‘stones’, where ‘stones[i]’ represents the number of stones in ‘ith’ piles. You are also given an integer ‘K’. Your task is to merge stones into one pile with minimum cost. In one operation you can take exactly ‘K’ consecutive piles and merge them and the cost of merging piles of stones in a particular operation is the total number of stones in all piles considered in that operation.

If it is not possible to merge, return -1.
For example:

You are given ‘stones’ = [4, 3, 4, 2, 5] and ‘K’ = 3, Here one way you can first merge [3, 4, 2] with a cost of 9, to form the array [4, 9, 5] then merge these piles as [18], with a cost of 18. The total cost to merge the array is 27, which is the minimum of all the possible ways. Hence the answer is 27.

**Examples:**
```
Sample Input 1:
2
5 3
4 3 4 2 5
3 2
1 2 3

Sample Output 2:
27
9

Explanation:
For the first test case, ‘stones’ = [4, 3, 4, 2, 5] and ‘K’ = 3, Here one way you can first merge [3, 4, 2] with a cost of 9, to form the array [4, 9, 5] then merge these piles as [18], with a cost of 18. The total cost to merge the array comes 27, which is the minimum. Hence the answer is 27.
For the second test case, ‘stones’ = [1, 2, 3] and ‘K’ = 2, Here is one way you can first merge [1, 2] with a cost of 3, to form the array [3, 3], then merge these piles [6], with a cost of 6. The total cost to merge the array comes 3 + 6 = 9, which is the minimum. Hence the answer is 9.

Sample Input 2:
2
3 3
5 8 9
5 4
4 5 3 2 3

Sample Output 2
22
-1
```

**Constraints:**
```
1 <= T <= 10
1 <= |N| <= 10^2
2 <= K <= N
1 <= |stones| <= 10^5

Time Limit: 1 sec.
```

### Editorial
https://www.naukri.com/code360/problems/merging-stones_3210617?leftPanelTabValue=SOLUTION
## Daily History
- Dec 8, 2024