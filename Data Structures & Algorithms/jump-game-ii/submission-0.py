class Solution:
    def jump(self, nums: List[int]) -> int:
        #

        l = 0
        r = 0
        min_jump = 0

        while r < len(nums) - 1:
            furthest_tracker = 0
            for i in range(l, r + 1, 1):
                furthest_tracker = max(furthest_tracker, i + nums[i])
            l = r + 1
            r = furthest_tracker
            min_jump += 1
        
        return min_jump