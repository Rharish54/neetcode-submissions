class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for elem in nums:
            if elem not in hmap:
                hmap[elem] = 1
            else:
                hmap[elem] += 1
        print(hmap)
        count = k
        res = []
        curr = 0
        value = 0
        while count > 0:
            for item in hmap:
               if hmap[item] > curr:
                curr = hmap[item]
                value = item
            res.append(value)
            smth = hmap.pop(value, None)
            count -= 1
            curr = 0
        return res