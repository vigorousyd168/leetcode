# 322 Coin Change
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        MAX = amount + 1
        dp = [0] + [MAX] * amount
        for i in xrange(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                m = MAX
                for c in coins:
                    if i - c >= 0:
                        m = min(dp[i-c]+1, m)
                dp[i] = m
        return dp[-1] if dp[-1] != MAX else -1

def main():
    sol = Solution()
    print sol.coinChange([1,2,5], 11) # 3
    print sol.coinChange([], 10) # -1
    print sol.coinChange([0], 1) # -1
    print sol.coinChange([1], 0) # 0
if __name__ == '__main__':
    main()