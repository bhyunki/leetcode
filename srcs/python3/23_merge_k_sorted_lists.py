# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        root = result = ListNode(None)
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        
        #print(h)
        
        while h:
            (v, i) = heapq.heappop(h)
            #print(v, i, lists[i])
            result.next, lists[i] = lists[i], lists[i].next
            result = result.next
            
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
            
        #print(root.next)
        
        return root.next
