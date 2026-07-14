class Solution:
    def rob(self, nums: List[int]) -> int:
        
        r1, r2 = 0, 0

        # visualization: [r1, r2, n, n+1, ...]
        # so you can see, to rob n we add r1 and NOT r2 bc adj
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp
        
        return r2

        
        return temp