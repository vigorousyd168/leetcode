# 188 Best Time to Buy and Sell Stock IV
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return 0
        if k >= l/2: # special handling for very large k
            res = 0
            for i in xrange(1, l):
                if prices[i] - prices[i-1] > 0:
                    res += prices[i] - prices[i-1]
            return res
        dpCurr = [0] * l
        dpPrev = [0] * l
        # dp[kk][i] = max(dp[kk][i-1], dp[kk-1][j] - prices[j] + prices[i]) - for any j < i
        for kk in xrange(1, k+1):
            tmpMax = dpPrev[0] - prices[0]
            for i in xrange(1, l):
                dpCurr[i] = dpCurr[i-1] if dpCurr[i-1] >= tmpMax + prices[i] else tmpMax + prices[i]
                #tmpMax = tmpMax if tmpMax >= dpPrev[i] - prices[i] else dpPrev[i] - prices[i]
                if dpPrev[i] - prices[i] > tmpMax:
                    tmpMax = dpPrev[i] - prices[i]
            dpPrev = dpCurr[:]
        return dpCurr[-1]
