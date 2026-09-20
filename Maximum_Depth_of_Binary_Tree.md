## Step 1: Understand the problem

Problem: 
- Given the root of a binary tree, return its depth (number of nodes along the longest path from the root to the furthest leaf)

Constraints:
- Tree can be empty

## Step 2: Working through the problem

First thought:
- Make a recursive function exploring left and right childs, stop that the bottom and 1, and while recursing back up, choose max of left and right

- Correct and did this in 4 mins! (I mean it was not complicated but still)

## Step 3: Plain English Algo

if not root:
    return 0

return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

