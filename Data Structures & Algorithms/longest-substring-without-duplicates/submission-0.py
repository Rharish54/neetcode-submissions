class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elem = set()
        l = 0
        tracker = 0

        for r in range(len(s)): #iterated from i = 0 -> len(s) -1
            while s[r] in elem:
                elem.remove(s[l])
                l += 1
            elem.add(s[r])
            tracker = max(tracker, r - l + 1)
        
        return tracker