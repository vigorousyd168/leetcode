# 120 Triangle
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        if l == 0:
            return 0
        dp = [triangle[0][0]] + [0] * (l-1)
        for i in xrange(1,l): # level i (1..l-1)
            dp[i] = triangle[i][i] + dp[i-1] # last number in current level
            for j in xrange(i-1, 0, -1):
                dp[j] = triangle[i][j] + (dp[j] if dp[j] < dp[j-1] else dp[j-1])
            dp[0] += triangle[i][0]
        return min(dp)

def main():
    sol = Solution()
    print sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) # 11
if __name__ == '__main__':
    main()