# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # start at curr

        temp = []

        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(temp) - 1
        currMax = 0

        while r > l:
            currMax = max(currMax, temp[l]+temp[r])
            l += 1
            r -= 1
        
        return currMax