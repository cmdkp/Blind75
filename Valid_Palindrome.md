## Step 1: Understand the problem

Problem: 
- Given a string s, return true if it is a palendrome (a string that reads the same forward and backwards)

Constraints:
- case sensitivity does not matter, and all non-alphanumerica characters are ignored
- s is made up of only ASCII characters

## Step 2: Working through the problem

First thought:
- Go through the string the first time and create a new string without the spaces or any characters that are not alphanumeric
- Then return newstring == newstring[::-1]

Second thought:
- Two pointer approach. skip any characters that are not alnum while going to middle. Stop when ptr1>ptr2.


## Step 3: Plain English Algo

newstring  = ''
for c in s:
    if c.isalnum():
        newstring = newstring + c.lower()

return newstring == newstring[::-1]
