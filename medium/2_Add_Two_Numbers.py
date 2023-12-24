class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        l3 = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            sum_vals = v1 + v2 + carry
            l3.next = ListNode(sum_vals % 10)
            carry = sum_vals // 10
            l3 = l3.next
        return dummy.next
