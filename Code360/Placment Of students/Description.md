# Question 

_Difficulty: Moderate_

The coordinator of the placement cell has received many applications of students applying in different companies. There are M students and N companies who are offering jobs. Each student is interested in a particular number of companies for a job. Each job opening can only accept one student and a student can only have 1 job. As a placement coordinator, you want to place a maximum number of students.

Your task is to find the maximum number of students that can be placed in one of their desired jobs

The data about the set of favourable jobs are given in the form of an M * N binary matrix named ‘mat’, i.e for M students we have M rows each having N integers. Now for example if the first candidate is interested in job1 the value of mat[i][j] will be 1 otherwise it will be 0.
Note:

It is possible that a single candidate is interested in multiple jobs but he can take up only one of the job out of his favourable jobs, also there is no priority in jobs, i.e all favourable jobs are equally favourable to the candidate

**Examples:**
```
Sample Input 1:
2
3 2
1 0
0 1
0 0
4 4
0 0 1 1
1 1 1 1
0 0 0 1
1 0 0 0

Sample Output 1:
2
4

Explanation of Sample Input 1:
Test Case 1: 
We see that we have 3 candidates and 2 jobs. 
Candidate 1 wants jobs 1 only
Candidate 2 wants job 2 only
Candidate 3 does not like any job
So, with this given arrangement, we can have that candidate 1 gets a job1 and candidate 2 gets job 2. So we placed 2 candidates. Hence we return 2.

Test Case 2:
We have 4 candidates and 4 jobs
Candidate 1 wants jobs 3 or jobs 4.
Candidate 2 wants any of the 4 jobs (pretty desperate)
Candidate 3 wants only job 4 
Candidate 4 wants only job 1

So with this arrangement, we can have candidate 1 with job 3, candidate 2 with job 2 candidates 3 with job 4, and candidate 4 with job 1.
Hence we placed all the candidates, hence we return 4.

Sample Input 2:
2 
3 4
1 1 1 1
1 1 1 1
1 1 1 1
6 6
0 1 1 0 0 0
1 0 0 1 0 0
0 0 1 0 0 0
0 0 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 1

Sample Output 2:
3
5
```

**Constraints:**
```
1 <= T <= 100
1 <= M * N <= 3000

Time Limit: 1sec
```

### Editorial
https://www.naukri.com/code360/problems/placment-of-students_1062591?leftPanelTabValue=SOLUTION

## Daily History
- Dec 15, 2024