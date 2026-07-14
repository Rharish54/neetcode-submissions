class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = 0
        l = 0
        r = l + 1

        while l < len(nums) and r < len(nums):
            if nums[l] == nums[r]:
                return nums[l]
            if r == len(nums) - 1:
                l += 1
                r = l + 1
                continue
            
            r += 1

        