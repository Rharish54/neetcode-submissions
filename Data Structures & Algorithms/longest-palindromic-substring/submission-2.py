class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        len_res = 0

        for i in range(len(s)):
            # odd length check
            l, r = i, i
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if (r - l + 1) > len_res:
                    res = s[l:r+1]
                    len_res = len(res)
                l -= 1
                r += 1

            # even length

            l, r = i, i + 1
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if(r - l + 1) > len_res:
                    res = s[l:r+1]
                    len_res = len(res)
                l -= 1
                r += 1
        
        return res
