# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
            
        if not list2: 
            return list1
            
        rtnhead = ListNode()
        rtncurr = rtnhead

        l1curr = list1
        l2curr = list2

        while l1curr and l2curr:
            next1 = l1curr.next
            next2 = l2curr.next
            
            if l1curr.val <= l2curr.val:
                rtncurr.next = l1curr
                rtncurr = rtncurr.next
                
                l1curr = next1
            
            else:
                rtncurr.next = l2curr
                rtncurr = rtncurr.next

                l2curr = next2 

        if not l1curr and l2curr:
            rtncurr.next = l2curr
        elif l1curr and not l2curr:
            rtncurr.next = l1curr

        return rtnhead.next
                
                
# Faster solution by just cleaning up last one.:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        rtnhead = ListNode()
        rtncurr = rtnhead

        while list1 and list2:
            
            if list1.val <= list2.val:
                rtncurr.next = list1
                list1 = list1.next
            
            else:
                rtncurr.next = list2
                list2 = list2.next 
            
            rtncurr = rtncurr.next

        rtncurr.next = list1 or list2

        return rtnhead.next
                
