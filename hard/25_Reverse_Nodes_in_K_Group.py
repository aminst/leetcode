# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, start, next_node):
        cur = start
        prev = None
        while cur != next_node:
            temp = cur.next
            if cur == start:
                cur.next = next_node
            else:
                cur.next = prev
            prev = cur
            cur = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start_pointer = head
        end_pointer = head
        count = 0
        new_head = None
        prev = None
        while end_pointer != None:
            count += 1
            if count == k:
                count = 0
                end_pointer = end_pointer.next
                h = self.reverse(start_pointer, end_pointer)
                if new_head == None:
                    new_head = h
                if prev != None:
                    prev.next = h
                prev = start_pointer
                start_pointer = end_pointer
            else:
                end_pointer = end_pointer.next
        return new_head


"""
Question and assumptions:
    * You can't change the values; you should change the nodes
    * reverse k at a time
    * k is smaller or equal to the length of list
    * if something is left that is less than k don't touch the remaining part
    * in place: yes

Examples:
    1 2 3 4 5 6 k = 5
    6 5 4 3 2 1

    1 4 5 3 2 1 k = 2
    4 1 3 5 1 2

Trivial Solution:
    * Have two pointers: start,  end
    * Go forward until end and start has a distance of k or you have reached end
    * reverse that part (how?)
        * 
    
    1 2 3 ->
    keep next part
    3 -> 2 -> 1 -> next
    reverse(start, end)

"""
