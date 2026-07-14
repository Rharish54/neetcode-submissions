class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        sets = set(s)

        for c in sets:
            count = l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l+= 1

                output = max(output, r - l + 1)
        
        return output