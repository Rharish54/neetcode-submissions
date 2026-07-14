class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in compMap:
                return [compMap.get(difference, 0), i]
            compMap[value] = i