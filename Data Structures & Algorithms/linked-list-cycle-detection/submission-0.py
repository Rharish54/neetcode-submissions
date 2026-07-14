# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # iterate through linked list
        # if (n) -> 1 ... n - 1, then return true, else false

        curr = head
        my_set = set()
        while curr.next:
            if curr not in my_set:
                my_set.add(curr)
            else:
                return True
            
            curr = curr.next

        return False