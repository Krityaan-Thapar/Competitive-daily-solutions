# Question 

_Difficulty: Easy_

Takahashi has a garden with ‘n’ beautiful flowers in a row. He waters exactly “arr[i]” liters of water to ith flowers from left to right daily to keep them beautiful. He has a container that can contain ‘k’ liters of water. But he follows certain rules to water all the plants:

Water a plant if he has sufficient water in the container, otherwise refill it.

You can only refill at the water tank which is placed one step before the first flower.

Takahashi wants to know the minimum number of steps he needs to water all the flowers.
For Example :

Let arr = {3, 5, 1, 2}, k = 6

Now in this example, he will first move to the first flower and water it. Now his container contains only 3 liters of water, hence he will refill the container, so he goes 1 step back and refills, comes to the 2nd flower, after watering the second flower, he still has 1 liter of water and 1 flower left. So he will water that flower and return to refill. Now he will come to the last flower and water it. 
Hence the total steps taken are: 1 + 1 + 2 + 1 + 3 + 4 = 12.

**Examples :**
```
Sample Input 1 :
2
3 11
3 2 5
3 5
4 2 1

Sample Output 1 :
3
5

Explanation For Sample Output 1 :
In the first example, he will first move to the first flower and water it, after that he is left with 8 liters of water, now he will move to the second flower and water it, after watering it he is still left with 6 liters of water which is enough for the third flower, so he will move to the third flower. Hence the total steps taken is 3.

In the second example, he will first move one step to water the first flower, now he is left with only one liter of water, so he will return to the water tank i.e. 1 step behind, and then come to the second flower, water it and move to the third flower, hence the total steps taken are 5.

Sample Input 2 :
2
5 9
4 7 2 6 1
5 1
1 1 1 1 1    

Sample Output 2 :
13
25
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 10^4
1 <= k <= 10^5
1 <= arr[i] <= k
Time limit: 1 sec
```

### Editorial
https://www.naukri.com/code360/problems/watering-flowers_2264968?leftPanelTabValue=SOLUTION

## Daily History
- Dec 9, 2024