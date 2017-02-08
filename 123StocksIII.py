# 123 Best Time to Buy and Sell Stock III
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        p = [0] * l
        if l == 0:
            return 0
        left_min, right_max = prices[0], prices[-1]
        left_profit, right_profit = 0, 0
        for i in xrange(1, l):
            if prices[i] < left_min:
                left_min = prices[i]
            elif prices[i] - left_min > left_profit:
                left_profit = prices[i] - left_min
            p[i] += left_profit
        for i in xrange(l-2, -1, -1):
            if prices[i] > right_max:
                right_max = prices[i]
            elif right_max - prices[i] > right_profit:
                right_profit = right_max - prices[i]
            p[i] += right_profit
        return max(p)

def main():
    sol = Solution()
    print sol.maxProfit([6,9,2,5,3,17,10,18,15]) # 23
    print sol.maxProfit([]) # 0
    print sol.maxProfit([1]) # 0
    print sol.maxProfit([3,2,1,]) # 0
    print sol.maxProfit([1,2,1,2,1,2]) # 2
    print sol.maxProfit([6,1,3,2,4,7]) # 7
if __name__ == '__main__':
    main()