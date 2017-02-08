# 174 Dungeon Game
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0:
            return 1 # error
        n = len(dungeon[0])
        if n == 0:
            return 1 # error
        dp = [[2147483647] * (n+1) for _ in xrange(m+1)]
        dp[-1][-2] = 1
        dp[-2][-1] = 1
        for i in xrange(m-1, -1 ,-1):
            for j in xrange(n-1, -1, -1):
                dp[i][j] = (dp[i+1][j] if dp[i+1][j] <= dp[i][j+1] else dp[i][j+1]) - dungeon[i][j]
                if dp[i][j] <= 0:
                    dp[i][j] = 1
        return dp[0][0]

def main():
    sol = Solution()
    print sol.calculateMinimumHP([[-2,-3,3], [-5,-10,1], [10,30,-5]]) # 7
if __name__ == '__main__':
    main()