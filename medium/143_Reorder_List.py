# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse_list(self, head):
        if head == None: return None, None
        if head.next == None:
            node = ListNode(head.val)
            return node, node
        next_reversed_head, next_reversed_tail = self.reverse_list(head.next)
        next_reversed_tail.next = ListNode(head.val)
        next_reversed_tail = next_reversed_tail.next
        return next_reversed_head, next_reversed_tail
    
    def get_mid(self, head):
        slow_cur = head
        fast_cur = head.next
        while fast_cur and fast_cur.next:
            slow_cur = slow_cur.next
            fast_cur = fast_cur.next.next
        return slow_cur

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.get_mid(head)
        past_mid = mid.next
        mid.next = None
        rev = self.reverse_list(past_mid)[0]

        first_curr = head
        second_curr = rev
        while second_curr:
            tmp_first_curr_next = first_curr.next
            tmp_second_cur_next = second_curr.next
            first_curr.next = second_curr
            second_curr.next = tmp_first_curr_next
            first_curr = tmp_first_curr_next
            second_curr = tmp_second_cur_next
