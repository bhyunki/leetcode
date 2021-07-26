# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n=ListNode()
        p=n
        
        while True:
            if not l1:
                n.next=l2
                break
            if not l2:
                n.next=l1
                break
        
            if l1.val < l2.val:
                n.next, l1 = l1, l1.next
            else:
                n.next, l2 = l2, l2.next
        
            n=n.next
        
        return p.next
