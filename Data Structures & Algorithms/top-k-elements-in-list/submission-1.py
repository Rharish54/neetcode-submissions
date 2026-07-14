class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #based on k = number of outputs

        count = {} #hashmap
        frequency = [[] for i in range(len(nums) + 1)]
        #list of lists of side len(nums) + 1:
        # [ [], [], [], ..., [] ]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            frequency[c].append(n)

        output = []

        for i in range(len(frequency) - 1, 0, -1):
            # iterates thru starting at last index to 0 exclusive
            for n in frequency[i]:
                output.append(n)
                #if the output is of size k, we reached capacity
                if len(output) == k:
                    return output
            





