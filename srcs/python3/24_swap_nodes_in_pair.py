# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        a=head
        if not a:
            return head
        b=head.next
        if not b:
            return head
        root=p=ListNode()
        while a and b:
            a.next, b.next, p.next = b.next, a, b
            a,p=a.next,a
            if a:
                b=a.next
        return root.next
            
