## Step 1: Understand the problem

Problem: Give a string consisting of: (, ) ,{, }, [, ]. Need to check if every open bracket is closed by the same type of close bracket, open brackets are closed in correct order, every close bracket has a cooresponding open bracket of the same type

Constraints:
- s is not empty
- s only consists of the brackets

## Step 2: Working through the problem

First thought:
- Use a stack, append if is an open bracket, pop if it is the right type of close bracket. 


## Step 3: Plain English Algo
Base case: empty string is true

Create a stack array
create a dict with key=closebracket, value=openbracket

for b in s:
    if b in dict.values():
        arr.append(b)
    if b in dict and arr[-1] == dict[b]:
        arr.pop()
        
return len(arr) == 0

Some issues later found were: checking if arr was empty before doing arr[-1]
