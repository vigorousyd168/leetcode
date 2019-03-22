# 343 Integer Break
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        if n == 4:
            return 4
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        if n > 1:
            result *= n
        return result
