class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        pq = []
        res = []

        for p in points:
            x = p[0]
            y = p[1]
            p_val = math.sqrt(((x - 0)**2) + ((y - 0)**2))
            heapq.heappush(pq, (p_val, p))
        

        while k != 0:
            _, point = heapq.heappop(pq)

            res.append(point)
            k -= 1
        
        return res