class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r and l < len(s) and r >= 0:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[l].isalnum() != True:
                l += 1
            elif s[r].isalnum() != True:
                r -= 1
        
        return True