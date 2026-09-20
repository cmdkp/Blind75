## Step 1: Understand the problem

Problem: 
- Given the roots of two binary trees, root and subroot, return true if there is a subtree in root which has the tree of subroot. Otherwise, return false. 

- A tree itself can be considered a subtree


AFTER RUNNING CHECK, REALIZED THIS DETAIL:
- All the subroots decendents need to be considered and compared to root's decendents too. This means when subtree ends, the real tree must end there too

Constraints:
- Both trees have at least 1 node in them


## Step 2: Working through the problem

First thought:
- Stopping point has to be when the subroot tree's leafs are reached. So keep going down the root tree to see if you get to a subtree with root = subroot. From there, check if the subtree is the same as the one from subroot and lastly return false or the outcome from the subtree checks.


## Step 3: Plain English Algo

if not subroot:
    return True
    
if not root and subroot:
    return False
    
checksub = root.val == subroot.val

if checksub:
    l = self.isSubtree(root.left, subroot.left)
    r = self.isSubtree(root.right, subroot.right)
    
    return l and r
    

return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

