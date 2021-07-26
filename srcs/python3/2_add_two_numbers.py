# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=0
        head=p=None
        while l1 or l2 or a!=0:
            v1,v2=0,0

            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
                
            if p:
                p.next=ListNode()
                p=p.next
            else:
                p=ListNode()
                head=p

            s = v1+v2+a
            v = s%10
            a = int(s/10)
                        
            p.val=v
            
        return head
