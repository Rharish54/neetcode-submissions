class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        temp = sorted(nums)
        i = 0

        while i < len(temp):
            if temp[i] == temp[i+1]:
                i += 2
            else:
                return False
        
        return True