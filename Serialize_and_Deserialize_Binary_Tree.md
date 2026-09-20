## Step 1: Understand the problem

Problem: 
- Given a binary tree, we want to make two algorithms: (1) to serialize (flatten) it into a string and (2) to deserialize (reconstruct) the tree

Constraints:
- number or nodes in the tree can be 0
- node values are integers from -1000 to 1000


## Step 2: Working through the problem

First thought:
- Since goal is just to store the tree in a 1d object, it can simply be traversed, and saved in the way the nodes and their values are reached. Can seperate the values with a comma, and follow the same traversal pattern when recontructing


## Step 3: Plain English Algo


serialize(self, root):

if not root.val:
    return ''
    
rtn = root.val + ','
rtn = rtn + serialize(root.left) + serialize(root.right)

return rtn


deserialize(self, data):

if data == '':
    return None

strval = data.split(',', 1)
rtn = TreeNode(int(strval))

l = data.split(',', 1)
r = data.split(',', 1)

rtn.left = deserialize(l)
rtn.right = deserialize(r)

return rtn
