import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap : k : v where k = number, v = occurence 
        # then convert to heap?

        hm = defaultdict(int)
        hp = []
        for i, n in enumerate(nums):
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] += 1
        
        for ky, v in hm.items():
            heapq.heappush(hp, [-v, ky])

        i = 0
        res = []
        while i < k:
            _, val = heapq.heappop(hp)
            res.append(val)
            print(res)
            i += 1
        return res

                