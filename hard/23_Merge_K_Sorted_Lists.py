# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import heapify, heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        final = dummy
        min_heap = []
        
        for i, node in enumerate(lists):
            if node != None:
                min_heap.append((node.val, i))
                lists[i] = lists[i].next
        heapify(min_heap)

        while min_heap:
            cur_min, index = heappop(min_heap)
            final.next = ListNode(cur_min)
            final = final.next
            if lists[index] != None:
                heappush(min_heap, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next
