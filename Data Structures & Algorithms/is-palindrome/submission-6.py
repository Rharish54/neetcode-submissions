class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = s.strip()
        txtLower = txt.lower()
        temp = []
        for c in txtLower:
            if c.isalnum():
                temp.append(c)
        l = 0
        r = len(temp) - 1
        while l <= r:
            if temp[l] == temp[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True