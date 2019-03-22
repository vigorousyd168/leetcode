# 121 Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, res = 2147483647, 0
        for p in prices:
            res = p - low if p - low > res else res
            low = p if p < low else low
        return res
def main():
    sol = Solution()
    print (sol.maxProfit([7, 1, 5, 3, 6, 4]))
if __name__ == '__main__':
    main()