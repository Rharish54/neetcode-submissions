class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        r3, r4 = 0, 0
  

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums) - 1):
            temp = max(r1 + nums[i], r2)
            r1 = r2
            r2 = temp
        
        for i in range(1, len(nums), 1):
            temp2 = max(r3 + nums[i], r4)
            r3 = r4
            r4 = temp2
        
        return max(temp, temp2)

        
