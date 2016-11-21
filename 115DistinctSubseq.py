# 115 Distinct Subsequences
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls, lt = len(s), len(t)
        if ls < lt:
            return 0
        prev = [1] * (ls+1)
        curr = [0] * (ls+1)
        for i in xrange(1, lt+1):
            curr = [0] * (ls+1)
            for j in xrange(i, ls+1): # start from i, no need to compute dp[i][0]..dp[i][i-1]
                curr[j] = (curr[j-1] + prev[j-1]) if t[i-1] == s[j-1] else curr[j-1]
            prev = curr[:]
        return curr[-1]
    def numDistinct_2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls, lt = len(s), len(t)
        if ls < lt:
            return 0
        dp = [[0] * (ls+1) for _ in xrange(lt+1)]
        # first row
        dp[0] = [1] * (ls+1)
        for i in xrange(1, lt+1):
            for j in xrange(i, ls+1): # start from i, no need to compute dp[i][0]..dp[i][i-1]
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) if t[i-1] == s[j-1] else dp[i][j-1]
            if dp[i][-1] == 0:
                return 0
        return dp[-1][-1]
def main():
    sol = Solution()
    print sol.numDistinct("abbcc","abc") # 4
    print sol.numDistinct("abc","cc") # 0
    print sol.numDistinct("abababab","ab") # 10
if __name__ == '__main__':
    main()