# Question 

_Difficulty: Moderate_

You are given a binary matrix with ‘M’ rows and ‘N’ columns initially consisting of all 0s. 'Q' queries follow. The queries can be of 4 types:

Query 1: 1 R index
Query 2: 1 C index 
Query 3: 2 R index
Query 4: 2 C index

In each query, the first input is the type of the query, the second input is whether we have to consider the row ('R') or the column ('C') and the third input is the index of the row/column. 

For each type 1 query, we need to flip the elements of the row/column having the given index. 

For each type 2 query, we have to output the number of zeros present in the row/column having the given index. 

Note:

Note that the matrix is a binary matrix, meaning that it only contains either 0 or 1.

**Examples :**
```
Sample Input 1:
2
3 3
3
1R1
1R2
2C1
2 2
1
2R1

Sample Output 1:
1
2

Explanation of Sample Output 1:
In test case 1, Next query 2C1 will return the count of the number of zeroes in the 1st column: 1
The change in the matrix after the first and second queries would look like this:
In test case 2, all the matrix elements are zero and hence the count of zeroes will be 2 for the first row.

Sample Input 2:
2
3 3
4
2C1
1R1
1R1
2R1
2 2
5
2C1
1R1
1R1
1R1
2R1

Sample Output 2:
3 3
2 0

Explanation of Sample Output 2:
In test case 1, 
First query 2C1 will return the count of the number of zeroes in the 1st column: 3
Next query 2R1 will return the count of the number of zeroes in the 1st column: 3
The change in the matrix after the second and third queries would look like this:

In test case 2,
First query 2C1 will return the count of the number of zeroes in the 1st column: 2
Next query 2R1 will return the count of the number of zeroes in the 1st column: 0
The change in the matrix after the second and third queries would look like this:
```

**Constraints:**
```
1 <= T <= 10
1 <= M, N  <= 100
1 <= Q <= 1000
1 <= R <= M
1 <= C <= N
type = 1, 2

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/query-and-matrix_1263845?leftPanelTabValue=SOLUTION

## Daily History
- Nov 30, 2024