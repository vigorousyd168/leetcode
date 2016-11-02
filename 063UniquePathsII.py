# 063 Unique Paths II
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # in place
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1: # dead game
            return 0
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j:] = [0] * len(obstacleGrid[0][j:])
                break
            obstacleGrid[0][j] = 1
        blocked = False
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                blocked = True
            obstacleGrid[i][0] = 0 if blocked else 1
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
def main():
    sol = Solution()
    print (sol.uniquePathsWithObstacles([[0]])) # 1
    print (sol.uniquePathsWithObstacles([[0],[0]])) # 1
    print (sol.uniquePathsWithObstacles([[0],[1]])) # 0
if __name__ == '__main__':
    main()