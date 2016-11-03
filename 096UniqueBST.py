# 096 Unique Binary Search Trees
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1,2,5]
        if n <= 0:
            return 0
        if n <= 3:
            return dp[n]
        k = 4
        while k <= n:
            s = 0
            for i in range(k/2):
                s += 2 * dp[i] * dp[k-1-i]
            if k & 1:
                s += dp[k/2] * dp[k/2]
            dp.append(s)
            k += 1
        return dp[-1]

def main():
    sol = Solution()
    print sol.numTrees(1) # 1
    print sol.numTrees(2) # 2
    print sol.numTrees(3) # 5
    print sol.numTrees(4) # 14
    print sol.numTrees(10) # 16796
if __name__ == '__main__':
    main()