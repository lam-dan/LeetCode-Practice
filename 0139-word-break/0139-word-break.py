class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in words:
                if s.startswith(word, i):
                    new_idx = i + len(word)
                    if dfs(new_idx):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)




            











        dfs(0)