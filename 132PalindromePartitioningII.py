# 132 Palindrome Partitioning II
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l <= 1:
            return 0
        dp = [0] * l
        pal = [[False] * l for _ in xrange(l)]
        for i in xrange(l):
            pal[i][i] = True
        for i in xrange(l):
            minCnt = i
            for j in xrange(i+1):
                if s[i] == s[j] and (j+1 >= i-1 or pal[j+1][i-1]):
                    pal[j][i] |= True
                    # if s[0:i+1] is a palindrome, 0 cut
                    minCnt = 0 if j == 0 else min(minCnt, dp[j-1]+1)
            dp[i] = minCnt
        return dp[-1]

def main():
    sol = Solution()
    print sol.minCut("") # 0
    print sol.minCut("a") # 0
    print sol.minCut("abb") # 1
    print sol.minCut("aab") # 1
    print sol.minCut("ababbbabbaba") # 3
if __name__ == '__main__':
    main()