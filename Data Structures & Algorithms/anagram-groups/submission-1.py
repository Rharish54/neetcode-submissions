class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashingPractice = defaultdict(list)

        for string in strs:
            count = 26 * [0]

            for char in string:
                count[ord(char) - ord("a")] += 1
            
            hashingPractice[tuple(count)].append(string)
        
        return hashingPractice.values()
