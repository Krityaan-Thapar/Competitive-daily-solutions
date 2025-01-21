# Question 

_Difficulty: Hard_

There are ‘N’ baskets, each containing some fruits. All baskets are placed in a single horizontal line. Kevin and Mark both are very hungry and so, they want to eat the fruits as much as possible. They have decided to select a basket from either end of the line only (formally, first or the last basket in that line only) and eat all the fruits in that basket. They will pick the baskets alternatively.

You have to tell how many maximum fruits Kevin can eat if both of them pick and eat the fruits optimally.

Note:
Kevin will pick the basket first.

**Examples :**
```
Sample Input 1:
2
3
6 4 5
4  
5 8 2 1  

Sample Output 1:
10
9

Explanation of Sample Output 1:
In test case 1, Kevin will first select the front basket (containing 6 fruits) and then after Mark’s selection, he will pick fruits from the 2nd basket as Mark has already selected the 3rd basket.
In test case 2, The order of selection of baskets are as follows: -
Kevin - 4th (1), Mark - 1st (5), Kevin - 2nd (8), and Mark - 3rd (2).

Sample Input 2:
3
1
5
2
8 7
4
2 2 2 2     

Sample Output 2:
5
8
4

Explanation for Sample Output 2:
In test case 1, there is only one basket and therefore, Kevin can only eat 5 fruits.
In test case 2, there are two baskets and Kevin wants to eat maximum fruits therefore, he will select 1st basket.
In test case 3, all baskets have the same number of fruits and so, Kevin can eat 2 + 2 = 4 fruits.
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 100
1 <= BASKET[i] <= 10^4

Where 'BASKET[i]' denotes the number of fruits in the ith basket.

Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/fruits-and-baskets_1172174

## Daily History
- Jan 21, 2024