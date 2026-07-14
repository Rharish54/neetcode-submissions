class Solution:
    def isPalindrome(self, s: str) -> bool:

        temp = ""
        for c in s:
            if c.isalnum():
                temp = temp + c
        
        temp = temp.lower()
        l = 0
        r = len(temp) - 1

        while l <= r:
            if temp[l] == temp[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
