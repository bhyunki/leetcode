# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        o,e = ListNode(), ListNode()
        ro,re = o,e
        p = head
        
        if not head:
            return None
        
        while head.next and head.next.next:
            o.next, e.next, head  = head, head.next, head.next.next
            o,e = o.next, e.next
            
        o.next, e.next = head, head.next
        o.next.next = re.next
        
        return ro.next
