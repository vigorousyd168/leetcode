# 312 Burst Balloons
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) + 2 # add nums[-1] and nums[n]
        myNums = [1] + nums + [1]
        # dp[i][j] is the max number of coins one can get from balloons i+1...j+1
        # but balloon i+1 and balloon j+1 cannot be burst
        dp = [[0] * l for _ in xrange(l)]
        # k+1 = right - left + 1 is the length of the balloon chain we consider
        # compute from 3 to l. When k == 3, the coins we can get is 1*a*1 = a.
        for k in xrange(2, l):
            for left in xrange(0, l-k):
                right = left + k
                for i in xrange(left+1, right):
                    temp = dp[left][i] + myNums[left]*myNums[i]*myNums[right] + dp[i][right]
                    if temp > dp[left][right]:
                        dp[left][right] = temp
        return dp[0][l-1]

def main():
    sol = Solution()
    print sol.maxCoins([3,1,5,8]) # 167
    print sol.maxCoins([1]) # 1
    print sol.maxCoins([1,1]) # 2
if __name__ == '__main__':
    main()