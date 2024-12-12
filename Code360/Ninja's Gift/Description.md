# Question 

_Difficulty: Hard_

Ninja is going to visit her friend Mico. He is thinking to gift her a string. But he came to know that Mico only likes the string 'S'. Ninja already has a string 'K'. Now, Ninja can change the string 'K' in some other string by choosing any character in one move and change all its occurrence with any other lowercase English character. He can do this several times.

Help Ninja to find if he can change his string 'K' to string 'S', which Mico likes.
Note:

Both 'S' and 'K' contain only lowercase English characters.

For Example:

K = "aabb" and S = "bbcc"
Now Ninja can do the following changes:
- Change ‘b’ to ‘c’ -> “aacc”
- Change ‘a’ to ‘b’ -> “bbcc”

Hence Ninja can give Mico the desired gift.

**Examples :**

```
Sample Input 1:
2
aabcc
ccdaa
ninjas
coding

Sample Output 1:
True
False

Explanation For Sample Output 1:
Test case 1:
Here K=ccdaa and S=aabcc. Here we can change K into S by following conversions
Change ‘d’ to ‘b’ -> ccbaa
Change ‘a’ to ‘e’ -> ccbee
Change ‘c’ to ‘a’ -> aabee
Change ‘e’ to ‘c’-> aabcc

Test case 2:
It is not possible to change K to S by any number of conversions.

Sample Input 2
2
code
dope
acbz
acbza

Sample Output 2
True
False
```

**Constraints:**
```
1 <= T <= 5
1 <= |K|, |S| <= 10^5

Time Limit: 1 second
```

### Editorial
https://www.naukri.com/code360/problems/ninja-s-gift_1281433?leftPanelTabValue=SOLUTION

## Daily History
- Dec 12, 2024