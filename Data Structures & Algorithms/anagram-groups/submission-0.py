class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = defaultdict(list)
        
        for string in strs:
            count = [0] * 26

            for character in string:
                # finding distance away from "a"
                #ord() is used to find ASCII/unicode value
                count[ord(character) - ord("r")] += 1

            hMap[tuple(count)].append(string)
        
        return hMap.values()
