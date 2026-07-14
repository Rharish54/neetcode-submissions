class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for n in nums:
            if n not in hset:
                hset.add(n)
            else:
                return True
        
        return False
