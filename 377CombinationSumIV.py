# 377 Combination Sum IV
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        for i in xrange(1, target+1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
                elif i == num:
                    dp[i] += 1
        return dp[-1]

def main():
    sol = Solution()
    print sol.combinationSum4([1,2,3], 4) # 7
    print sol.combinationSum4([2], 1) # 0
if __name__ == '__main__':
    main()