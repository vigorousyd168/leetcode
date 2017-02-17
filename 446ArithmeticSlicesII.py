# 446 Arithmetic Slices II
from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[i] is a dict
        # dp[i][j] is the number of arithmetic sequences ending at A[i] with distance j
        #   *including sequences of length 2
        dp = [defaultdict(int) for _ in A]
        res = 0
        for i in xrange(1, len(A)):
            for j in xrange(i):
                step = A[i] - A[j]
                dp[i][step] += 1
                if step in dp[j]: # there exist >=1 arithmetic sequences ending at A[j] with distance step
                    res += dp[j][step]
                    dp[i][step] += dp[j][step]
        return res


def main():
    sol = Solution()
    print sol.numberOfArithmeticSlices([2,4,6,8,10]) # 7
    print sol.numberOfArithmeticSlices([1,2,3,5,8,9,10]) # 5
if __name__ == '__main__':
    main()