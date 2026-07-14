class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        new_s = sorted(s)
        final_s = "".join(new_s)

        new_t = sorted(t)
        final_t = "".join(new_t)
        return final_s == final_t
