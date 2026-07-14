class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #neetcode
        # neet, code
        # len - i = w || i + len(w) <= N
        # Note for the above equation, either work!
        # 4 + 4 <= 8

        # start at the end and comparatively check to see if 
        # we have a valid word in set wordDict

        n = len(s)
        # make our cache -> in this case its an array / table
        # cache is just a structure where we store past sub problems
        # it allows for us to not have to recompute them!
        dp = [False] * (n + 1)
        dp[n] = True
        # [F, F, ... , T] -> T is base case

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                # len(string) - i >= word
                if ((n - i) >= len(word)
                and s[i : i + len(word)] == word):
                    # initializing where a break COULD happen
                    dp[i] = dp[i + len(word)]
                # found valid word -> no need to check again!
                if dp[i] == True:
                    break
        # dp[0] is only true if we dp[0] + len(word) == TRUE
        # and this only happens if dp[0] + len(word) was 
        # at a word break. Therefore we have a valid word break!
        return dp[0]

