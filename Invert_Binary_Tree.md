## Step 1: Understand the problem

Problem: 
- Given the root of a binary tree, invert the binary tree (like swap left and right nodes) and return its root

Constraints:
- Tree can be empty


## Step 2: Working through the problem

First thought:
- Make a recursive function which goes through the tree and just swaps left and right nodes

NOTE: Don't forget the self. for calling functions internally/recursively in python
## Step 3: Plain English Algo

if not root:
    return root

root.left, root.right = invertTree(root.right), invertTree(root.left)

return root
