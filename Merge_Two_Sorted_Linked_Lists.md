## Step 1: Understand the problem

Problem: 
- Given the heads of two sorted linked lists, merge them into one big sorted linked list and return the new head.

Constraints:
- Length of each list can be 0


## Step 2: Working through the problem

First thought:
- Start with both heads, set a new head value called rtnhead and run a while loop to merge the lists until the end of one is reached. Then at the end just check if the other is empty too and if not then add the remaining node to the end of the rtn LL.

- Did not consider case where 
list1=[5]
list2=[1,2,4]

and so the algorithm must wait to input a value and not input it immediately. 
- But fix should be simple, instead of doing both inputs together like below, will do one per iteration.
- And this worked.

## Step 3: Plain English Algo

if not list1:
    return list2
    
if not list 2: 
    return list1
    
rtnhead = ListNode()
rtncurr = rtnhead

l1curr = list1
l2curr = list2

while l1curr and l12urr:
    next1 = l1curr.next
    next2 = l2curr.next
    
    if l1curr.val <= l2curr.val:
        rtncurr.next = l1curr
        rtncurr = rtncurr.next
        rtncurr.next = l2curr
        
        l1curr = l1curr.next
        l2curr = l2curr.next
    
    else:
        rtncurr.next = l2curr
        rtncurr = rtncurr.next
        rtncurr.next = l1curr
        
        l1curr = l1curr.next
        l2curr = l2curr.next      

if not l1curr and l2curr:
    rtncurr.next = l2curr
elif l1 curr and not l2curr:
    rtncurr.next = l1curr

return rtnhead.next
        
        
