# Minimum Path Sum
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # in place
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]
        return grid[m-1][n-1]
def main():
    sol = Solution()
    print sol.minPathSum([[0,0,0],[0,1,0],[0,0,0]]) # 0
if __name__ == '__main__':
    main()