class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # soln must have O(1) space

        l = 0
        r = len(numbers) - 1
        total = 0
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target and l!=r:
                return [l + 1, r + 1]
            
            elif total > target:
                r -= 1
            
            elif total < target:
                l += 1
            
            total = 0
            
