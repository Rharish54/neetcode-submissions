import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:

        self.nums.append(val)


        temp = [x * -1 for x in self.nums]

        heapq.heapify(temp)
        count = self.k
        res = 0
        while count > 0:
            res = heapq.heappop(temp) * - 1
            count -= 1
        
        return res

        
