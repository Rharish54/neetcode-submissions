class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up approach
        # space of O(n)
        if n == 1:
            return 1

        ar = [0] * (n + 1)
        ar[n] = 1
        ar[n - 1] = 1
        i = n - 2

        while i >= 0:
            ar[i] = ar[n] + ar[n-1]
            ar[n-1] = ar[n]
            ar[n] = ar[i]
            i -= 1
        
        return ar[0]