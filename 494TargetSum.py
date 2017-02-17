# 494 Target Sum
from collections import defaultdict
class Solution(object):
    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        non_zero_nums = [k for k in nums if k > 0]
        d = {0: 1}
        for n in non_zero_nums:
            td = defaultdict(int)
            for k, v in d.iteritems():
                td[k+n] += v
                td[k-n] += v
            d = td
        return 2 ** (len(nums) - len(non_zero_nums)) * d[S]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def subset_sum(nums, target):
            dp = [1] + [0] * target
            for n in nums:
                for s in xrange(target, n-1, -1):
                    dp[s] += dp[s-n]
            return dp[target]
        non_zero_nums = [n for n in nums if n > 0]
        diff = sum(non_zero_nums) - S
        if diff % 2 == 1 or diff < 0:
            return 0
        target = diff / 2
        # find any combinations of nums to sum up to target
        return 2 ** (len(nums) - len(non_zero_nums)) * subset_sum(non_zero_nums, target)

def main():
    sol = Solution()
    print sol.findTargetSumWays([43,1,49,22,41,1,11,1,24,10,26,49,33,4,20,19,44,42,2,37], 17) # 14
    print sol.findTargetSumWays([1,1], 1) # 0
    print sol.findTargetSumWays([1,1,1,1,1], 3) # 5
    print sol.findTargetSumWays([1,2,3,4], 0) # 2
    print sol.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,8], 8) # 1024
if __name__ == '__main__':
    main()