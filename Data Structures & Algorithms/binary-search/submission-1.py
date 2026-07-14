class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        middle = int(len(nums) / 2)

        #check if target is > to nums[middle], if so then ++, if not --

        while middle < len(nums) and middle >= 0:
            if nums[middle] > target:
                if middle - 1 < 0:
                    return -1
                if nums[middle - 1] < target:
                    return -1
                else:
                    middle = middle - 1
            elif nums[middle] < target:
                if(middle + 1 >= len(nums)):
                    return -1
                if nums[middle + 1] > target:
                    return -1
                else:
                    middle = middle + 1
            else:
                return middle
        
        return -1
