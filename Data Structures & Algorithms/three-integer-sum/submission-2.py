class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                tracker = n + nums[l] + nums[r]
                if tracker == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    #update pointer
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r-=1
                elif tracker > 0:
                    r -= 1
                else:
                    l += 1
        
        return res