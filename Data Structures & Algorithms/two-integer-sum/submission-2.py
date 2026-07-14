class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(nums):
            # format: index : number
            hmap[n] = i
        
        for i, n in enumerate(nums):
            difference = target - nums[i]
            # this checks to see if the difference is in the hashmap
            # and if the difference is not just the same value in the same index (ex: 6 - 3 = 3)
            if difference in hmap and hmap[difference] != i:
                return [i, hmap[difference]]
            