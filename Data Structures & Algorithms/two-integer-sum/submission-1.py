class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = l + 1
        res = []
        while l <len(nums) or r < len(nums):
            if nums[l] + nums[r] == target:
                res.append(l)
                res.append(r)
                return res
            if nums[l] + nums[r] != target:
                if r < len(nums) - 1:
                    r += 1
                else:
                    l += 1
                    r = l + 1
            