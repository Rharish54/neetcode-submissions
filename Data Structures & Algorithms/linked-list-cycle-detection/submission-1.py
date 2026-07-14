# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # iterate through linked list
        # if (n) -> 1 ... n - 1, then return true, else false

        # #NOTE: sets do not add the same value twice
        # i.e it will not add duplicated values. However,
        # this if two nodes have the same value in a linked list
        # they are not considered the same value as they are
        # different node objects with different ref to memory
        # thus set.add() will still add "duplicate" edge case
        curr = head
        my_set = set()
        while curr.next:
            if curr not in my_set:
                my_set.add(curr)
            else:
                return True
            
            curr = curr.next

        return False