# 140 Word Break II
class Solution(object):
    def dfs(self, idx):
        if self.s[idx:] in self.dp:
            return self.dp[self.s[idx:]]
        sentences = []
        if idx == self.ls:
            return [""] # [""] instead of [] so that the for suffix below works
        for i in xrange(idx, self.ls):
            if self.s[idx:i+1] in self.wordDict:
                for suffix in self.dfs(i+1):
                    sentences.append(self.s[idx:i+1] + (" " + suffix if suffix != "" else ""))
        self.dp[self.s[idx:]] = sentences
        return sentences
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.ls = len(s)
        if self.ls == 0 or len(wordDict) == 0:
            return []
        self.wordDict = wordDict
        self.s = s
        self.dp = {} # to save the string->sentence mapping
        return self.dfs(0)

def main():
    sol = Solution()
    print sol.wordBreak("catsanddog", {"cat", "cats", "and", "sand", "dog"}) # ["cats and dog", "cat sand dog"]
    print sol.wordBreak("abcd", ["a", "b", "abc", "cd"]) # ["a b cd"]
if __name__ == '__main__':
    main()