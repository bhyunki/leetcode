# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        i = 1
        root = ListNode(0, head)
        p = None
        l = root
        
        if left == right:
            return head
        
        while True:
            if i >= left and i <= right:
                #reverse list
                head.next, head, p = p, head.next, head
            elif i > right:
                l.next.next, l.next = head, p
                break
            else: # i < left
                l, head = l.next, head.next
            i+=1
            
        return root.next
