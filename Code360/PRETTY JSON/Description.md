# Question 

_Difficulty: Easy_

You are given a string 'STR' representing JSON object. Return an array of strings denoting JSON objects with proper indentation.
Rules for proper indentation:

1. Every inner brace should increase one indentation to the following lines.
2. Every close brace should decrease one indentation to the same line and the following lines.
3. Every ‘,’ will mean a separate line.
4. The indents can be increased with an additional 4 spaces or ‘/t’.

Example:

Let the input be: "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"

Then we return the following array of strings: 
{ 
    A:"B",
    C: 
    { 
        D:"E",
        F: 
        { 
            G:"H",
            I:"J"
        } 
    } 
}

Note that for every new brace we are putting an additional 4 spaces or \t.

Note:
1. [] and {} are only acceptable braces in this case.

**Examples:**
```
Sample Input 1:
2
["foo", {"bar":["baz",null,1.0,2]}]
[{"EmployeeID":1,"Name":"Abhishek","Designation":"SoftwareEngineer"}]

Sample Output 1:
[
    "foo",

    {
        "bar":
        [
            "baz",
            null,
            1.0,
            2
        ]
    }
]
[
    {
        "Employee ID":1,
        "Name":"Abhishek",
        "Designation":"SoftwareEngineer"
    }
]

Explanation of sample input 1 :
Test Case 1:
In the first test case,
We can see that we have 3 braces so we print when we encounter ‘[‘ we indent by leaving 4 spaces and then put “foo” in the string. 
Then we indent 4 more spaces and put “bar”.
Finally, we indent 4 more spaces for the last opening brace and then print baz.
Since we have ‘,’ after ‘bazz’ we make a new line for null and the numbers. 
Finally, we close the brackets taking care of the proper indentation.

In the second test case,
We have 2 braces only. After the first ‘[‘ we leave 4 spaces and put ‘{‘ in the string.
Then we put the string data taking care to change the line after every ‘,’  and de-indent for every closing brace.

Sample Input 2:
1
{"EmployeeID":2,"Name":"Garima","Designation":"EmailMarketing Specialist"}

Sample Output 2:
{
    "Employee ID":2,
    "Name":"Garima",
    "Designation":"EmailMarketing Specialist"
}
```

**Constraints:**
```
1 <= T <= 100
1 <= N <= 2*10^3
```

### Editorial
https://www.naukri.com/code360/problems/pretty-json_1112618?leftPanelTabValue=SOLUTION

## Daily History
- Dec 8, 2024