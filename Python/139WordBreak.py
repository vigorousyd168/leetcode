# 139 Word Break
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        # dp[i+1] is True means there is a word seq ending at s[i]
        dp = [True] + [False] * len(s)
        for i in xrange(len(s)):
            for j in xrange(i, -1, -1):
                if dp[j] and s[j:i+1] in wordSet:
                    dp[i+1] = True
                    break
        return dp[-1]

def main():
    sol = Solution()
    print sol.wordBreak("leetcode", ["leet", "code"]) # True
    print sol.wordBreak("a", []) # False
    print sol.wordBreak("a", ["b"]) # False
    print sol.wordBreak("a", ["a"]) # False

if __name__ == '__main__':
    main()