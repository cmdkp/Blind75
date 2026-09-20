## Step 1: Understand the problem

Problem:
- Given the beginning of a singly linked list, head, reverse the list and return the new beginning of the list

Constraints:
- length of list can be 0


## Step 2: Working through the problem

First thought:
- Create an array with the values of the linked list and in reverse order just create a new linked list

Second thought:
- Keep assigning the current node its prevous node as its next. Will need to keep track of prev, curr and nextnode and consider edge cases of empty LL, LL of size 1, LL of size two and what happens at the end of the LL

- For a LL of size 1, nothing needs to be done. For a LL of size more than one:
    - start at node1 and assign it to prev, go to node2 and assign it to curr, if LL is only 2 nodes long or prev is head, simply point next of curr to prev, next of prev to None and be done. Otherwise, get next of node2 and assign it to nextnode. Set val of curr to prev and set prev to curr, curr to nextnode, and nextnode to curr.next. keep going until curr.next is None and then after setting its next to its prev, return it


## Step 3: Plain English Algo

if not head:
    return None

if head.next is None:
    return head

prev = None
curr = head
nextnode = None

while curr:
    nextnode = curr.next
    curr.next = prev
    
    prev = curr
    curr = nextnode

return prev
