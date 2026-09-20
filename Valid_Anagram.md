## Step 1: Understand the problem

- Given two strings s and t, return true if the two strings are anagrams (same letters different positions) of each other, otherwise return false. 

- Need to check if same letters in both strings

## Step 2: Working through the problem

First thought:
- Sort both strings by letters a->z and then in one for loop go through both strings checking if any letters are different at the same index.

Second thought:
- split string one into a list of chars. iterate through char of string two and pop char from list one if/when char in list. If char not in list, return false. If loop over and list not empty, return false. otherwise return true

dict

Third thought:
- Add chars of two strings into two set and just check if both sets the same


## Step 3: Plain English Algo

2N => O(N)

dict = {}   # key value pairs letter: number

if len(s) == len(t)

for i in range(len(s)):

    for the first string, check if letter at s[i] in dict, if it isn't, add it and number =1. if it is then number -1 
    
    repeat for second string
    

sum = sum({key in dict.getKeys})

return sum == 0



