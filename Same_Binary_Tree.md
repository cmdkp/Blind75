## Step 1: Understand the problem

Problem: 
- Given the roots of two binary trees, need to return true if the trees are equivalent (same nodes structure and values)
- So nodes will be different objects, but values are what to check

Constraints:
- Trees can be empty

## Step 2: Working through the problem

First thought:
- Since the function takes two parameters, can just go through the tree together


## Step 3: Plain English Algo

if not p and not q:
    return True
    
if p and q:
    
    vals = p.val == q.val
    l = self.isSameTree(p.left, q.left)
    r = self.isSameTree(p.right, q.right)
    
    return vals and l and r

return False
    
