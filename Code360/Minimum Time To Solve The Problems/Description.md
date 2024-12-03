# Question 

_Difficulty: Hard_

There are 'N' number of subjects and the ith subject contains subject[i] number of problems. Each problem takes 1 unit of time to be solved. Also, you have 'K' friends, and you want to assign the subjects to each friend such that each subject is assigned to exactly one friend. Also, the assignment of subjects should be contiguous. Your task is to calculate the maximum number of problems allocated to a friend is minimum. See example for more understanding.
For Example:

If N = 4, K = 2 and subjects = {50,100,300,400}
Assignment of problems can be done in the following ways among the two friends.
{} and {50,100,300,400}. Time required = max(0, 50+100+300+400) = max(0, 850) = 850
{50} and {100,300,400}. Time required = max(50, 100+300+400) = max(50, 800) = 800
{50, 100} and {300,400}. Time required = max(50+100, 300+400) = max(150, 700) = 700
{50,100,300} and {400}. Time required = max(50+100+300, 400) = max(450, 400) = 400
{50,100,300, 400} and {}. Time required = max(50+100+300+400, 0) = max(850, 0) = 850

So, out of all the above following ways, 400 is the lowest possible time.

**Examples :**
```
Sample Input 1:
1
3 1
20 12 40

Sample Output 1:
72

Explanation for sample 1:
For the first test case, there is only 1 possible way to do the assignment, i.e. {20, 12, 40}. So, the minimum time required is 20 + 12 + 40 = 72.

Sample Input 2:
2
4 8
30 50 40 100
4 2
12 20 50 60

Sample Output 2:
100
82

Explanation for sample 2:
For the first test case, there are 8 friends, but only 4 subjects. So each subject is assigned to one friend and the maximum time taken is max(30, 50, 40, 100) = 100.
For the second test case, the assignment of problems can be done in the following ways.
{} and {12,20,50,60}. Time required = max(0, 12+20+50+60) = max(0, 142) = 142
{12} and {20,50,60}. Time required = max(12, 20+50+60) = max(12, 130) = 130
{12, 20} and {50,60}. Time required = max(12+20, 50+60) = max(32, 110) = 110
{12,20,50} and {60}. Time required = max(12+20+50, 60) = max(82, 60) = 82
{12,20,50, 60} and {}. Time required = max(12+20+50+60, 0) = max(142, 0) = 142
So, out of all the above following ways, 82 is the lowest possible time. Hence, our answer is 82.
```

**Constraints:**
```
1 <= T <= 10 
1 <= N, K <= 10^4
1 <= subjects[i] <= 10^9   

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/minimum-time-to-solve-the-problems_1062659?leftPanelTabValue=SOLUTION

## Daily History
- Dec 3, 2024