## Step 1: Understand the problem

Problem: Given the beginning of a linked list (head), return true if there is a cycle in the linked list. Otherwise return false.

Constraints:
- Length of list can be 0
- It does not say, so assume node values can repeat

## Step 2: Working through the problem

First thought:
- Instructions say nothing about mutating the linked list so I could just set the val of a visited node to None, and if a None valued node is encountered again, then there is a loop and return true. If node.next = None is reached before that, then no loop and return false.


- OK, so this solution passed, but there was ofcourse a better way to detect cycles than to mutate the list. This solution only worked because mutation didn't matter. 

- The better way the solution shows is to use a hash set (just a set() in python) and store visited nodes in there. That way all you do each time is check if node in set or not. 

## Step 3: Plain English Algo

curr = head
while curr:
    if not curr.val:
        return True
    
    curr.val = None
    
    if not curr.next:
        return False
        
    curr = curr.next

return False


