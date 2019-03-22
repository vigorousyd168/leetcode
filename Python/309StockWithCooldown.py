# 309 Best Time to Buy and Sell Stock with Cooldown
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return 0
        sec = 0 if prices[0] >= prices[1] else prices[1] - prices[0]
        if l == 2:
            return sec
        # maxProfit, last transaction is buy, up to day i
        buy = [-prices[0]] + [max(-prices[1],-prices[0])] + [0] * (l-2)
        # maxProfit, last transaction is sell, up to day i
        sell = [0] + [max(0, prices[1] - prices[0])] + [0] * (l-2)
        for i in xrange(2,l):
            newBuy, newSell = max(sell[i-2] - prices[i], buy[i-1]), max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = newBuy
            sell[i] = newSell
        return sell[-1]

def main():
    sol = Solution()
    print sol.maxProfit([1,2,3,0,2]) # 3
    print sol.maxProfit([]) # 0
    print sol.maxProfit([1,2,3,0,2,3,0,7,6,4,3,2,1,0,6,5,0,7,4,2,9,8,5,9,6,8,2,1,0,2]) # 36
    print sol.maxProfit([2,1,2,1,0,1,2]) # 3
    print sol.maxProfit([1,2,4]) # 3
if __name__ == '__main__':
    main()