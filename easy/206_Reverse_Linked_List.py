# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        if head.next == None:
            node = ListNode(head.val)
            return node, node
        next_reversed_head, next_reversed_tail = self.reverse(head.next)
        next_reversed_tail.next = ListNode(head.val)
        return next_reversed_head, next_reversed_tail.next
        

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.reverse(head)[0]
