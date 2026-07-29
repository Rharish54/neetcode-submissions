class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        temp = ''.join(sorted(s1))

        #slice through the 

        for i in range(len(s2)):
            if i + n <= len(s2):
                val = s2[i:i+n]
                curr = ''.join(sorted(val))
                if curr == temp:
                    return True
        
            else:
                continue
        
        return False
