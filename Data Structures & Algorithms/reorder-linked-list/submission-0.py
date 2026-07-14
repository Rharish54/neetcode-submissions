# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #left pointer, right pointer, 

        left, right = head, head.next

        while right and right.next:
            left = left.next
            right = right.next.next

        middle = left.next
        left.next = None #last elem of list
        prev = None

        #reversing the last half of the linked list
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        #merging the two lists to complete the algo
        first, middle = head, prev
        while middle: 
            tmp1, tmp2 = first.next, middle.next
            first.next = middle
            middle.next = tmp1
            first = tmp1
            middle = tmp2

        


