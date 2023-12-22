# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        l, r = head, head.next
        while l and r and r.next:
            if l == r:
                return True
            l = l.next
            r = r.next.next
        return False
