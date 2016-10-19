# 172 Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        base = 5
        while base <= n:
            result += n/base
            base *= 5
        return result

def main():
    sol = Solution()
    print sol.trailingZeroes(1) # 0
    print sol.trailingZeroes(125) # 31

if __name__ == '__main__':
    main()