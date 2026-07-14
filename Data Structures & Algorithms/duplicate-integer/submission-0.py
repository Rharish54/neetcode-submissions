class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = []
        for n in nums:
            if n not in hset:
                hset.append(n)
            else:
                return True
        
        return False
