class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        temp = [-x for x in stones]

        while len(temp) > 1:
            heapq.heapify(temp)

            x = heapq.heappop(temp) * -1
            y = heapq.heappop(temp) * -1

            if x != y:
                stone = abs(x - y) * -1
                heapq.heappush(temp, stone)
            
        
        if temp:
            return temp[0] * -1
        else:
            return 0
            
