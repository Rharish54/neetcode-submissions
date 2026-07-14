class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hm = defaultdict(int)

        for h in hand:
            hm[h] += 1
        
        # make a min heap of the KEYS of our hash map
        min_heap = list(hm.keys())

        # 
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            # 1,2,3,4,5,6 , gs=4, 1-5
            for i in range(first, first + groupSize):
                if i not in hm:
                    return False
                hm[i] -= 1
                if hm[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True



        


