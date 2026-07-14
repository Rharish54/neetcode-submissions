class Solution:
    def isPalindrome(self, s: str) -> bool:

        # TWO POINTER SOLUTION
        l = 0
        r = len(s) - 1
        while l <= r and l < len(s) and r >= 0:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                if s[l].isalnum() != True:
                    l += 1
                if s[r].isalnum() != True:
                    r -= 1
        
        return True