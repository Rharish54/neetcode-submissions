class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate thru list, iterate thru string and see if it contains same strings
        # this created a dict where the default keys are of a type list 
        res = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            res[sortedStr].append(s)
        
        return list(res.values())