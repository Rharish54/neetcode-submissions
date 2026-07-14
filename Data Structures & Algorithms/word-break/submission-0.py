class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #neetcode
        # neet, code
        # len - i = w | i + len(w) <= N
        # 4 + 4 <= 8

        # start at the end and comparatively check to see if 
        # we have a valid word in set wordDict

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        # [F, F, ... , T] -> T is base case

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                # len(string) - i >= word
                if ((n - i) >= len(word)
                and s[i : i + len(word)] == word):
                    dp[i] = dp[i + len(word)]
                
                if dp[i] == True:
                    break
        
        return dp[0]

