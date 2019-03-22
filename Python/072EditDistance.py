# 072 Edit Distance
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        if l1 == 0 or l2 == 0:
            return l1 if l1 >= l2 else l2

        dp = [[0] * (l2+1) for _ in xrange(l1+1)]
        for j in xrange(l2+1):
            dp[0][j] = j
        for i in xrange(1, l1+1):
            dp[i][0] = i
            for j in xrange(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]

    def minDistance_b(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # LCS
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2+1) for _ in xrange(l1+1)]
        for i in xrange(l1):
            for j in xrange(l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = dp[i][j+1] if dp[i][j+1] >= dp[i+1][j] else dp[i+1][j]
        res, i, j = 0, l1, l2
        prev = [l1,l2] # to the right of LCS
        for p in dp:
            print p
        while i >= 1 and j >= 1:
            print "visiting", i, j
            if dp[i-1][j-1] == dp[i][j]:
                i, j = i-1, j-1
            else: # dp[i][j] = dp[i-1][j-1] + 1, 3 cases
                if dp[i][j] == dp[i-1][j]:
                    #if prev[0] - i < prev[1] - j: # do we keep j?
                    if j < i:
                        i, j = i-1, j
                        continue
                if dp[i][j] == dp[i][j-1]:
                    #if prev[0] - i > prev[1] - j: # do we keep i?
                    if j > i:
                        i, j = i, j-1
                        continue
                gap = max(prev[0]-i, prev[1]-j)
                prev = [i-1, j-1]
                i, j = i-1, j-1
                res += gap
        return res + max(prev[0],prev[1]) # to the left of LCS
def main():
    sol = Solution()
    print sol.minDistance("aefdf", "abcddfe") # 4
    print sol.minDistance("", "") # 0
    print sol.minDistance("aa", "") # 2
    print sol.minDistance("", "a") # 1
    print sol.minDistance("abcdf", "accfdf") # 2, which c matches matters
    print sol.minDistance("bcdfhgy", "ccfdfu") # 5
if __name__ == '__main__':
    main()
