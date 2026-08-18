# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # start at curr
        #[1, 2, 3, 4, 5, 6]
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now, curr is set to the START of second half

        prev = None
        curr = slow
        # need to accomplish 4 <- 5 <- 6
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        p1, p2 = head, prev
        res = 0

        while p1 and p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return res