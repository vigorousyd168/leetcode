# 375 Guess Number Higher or Lower II
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        MAX = 2147483647
        for i in xrange(n+1):
            row = [0] * (n+1)
            dp.append(row)
        # dp is (n+1) * (n+1) matrix
        for j in xrange(2, n+1):
            for i in xrange(j-1, 0, -1):
                minCost = MAX
                for g in xrange(i+1, j):
                    worstCostAtG = g + max(dp[i][g-1], dp[g+1][j])
                    if worstCostAtG < minCost:
                        minCost = worstCostAtG # min: best strategy
                dp[i][j] = i if j == i + 1 else minCost
        return dp[1][n]

def main():
    sol = Solution()
    print sol.getMoneyAmount(1) # 0
    print sol.getMoneyAmount(2) # 1
    print sol.getMoneyAmount(3) # 2
    print sol.getMoneyAmount(4) # 4
    print sol.getMoneyAmount(5) # 6
    print sol.getMoneyAmount(6) # 8
    print sol.getMoneyAmount(7) # 10, 12, 14, 16, 18
    print sol.getMoneyAmount(12) # 21, 24, 27, 30, 34, 38, 42, 46
    print sol.getMoneyAmount(20) # 49
if __name__ == '__main__':
    main()