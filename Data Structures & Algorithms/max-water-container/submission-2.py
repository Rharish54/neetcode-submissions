class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (r - l) * min(h[r], h[l])
        l, r = 0, len(heights) - 1

        total = 0

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            total = max(total, curr)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return total
            