import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1
        
        hp = []
        for ky, v in hm.items():
            heapq.heappush(hp, (-v, ky))
        
        print(hp)
        res = []


        for i in range(1, k + 1, 1):
            print("hello")
            _, key = heapq.heappop(hp)
            res.append(key)
        

        return res
            