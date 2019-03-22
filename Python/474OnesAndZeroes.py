# 474 Longest Increasing Subsequence
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in xrange(m+1)] 
        for s in strs:
            a = s.count('0')
            b = len(s) - a
            # desc because we don't want lower i, j to change first
            for i in xrange(m, a-1, -1):
                for j in xrange(n, b-1, -1):
                    if dp[i-a][j-b]+1 > dp[i][j]:
                        dp[i][j] = dp[i-a][j-b]+1
        return dp[m][n]

def main():
    sol = Solution()
    print sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) # 4
    print sol.findMaxForm(["10", "0", "1"], 1, 1) # 2
    print sol.findMaxForm(["111", "11", "1"], 10, 3) # 2
if __name__ == '__main__':
    main()