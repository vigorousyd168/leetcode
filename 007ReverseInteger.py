# 007 Reverse Integer
class Solution(object):
    max_int = 2**31
    min_int = -2**31-1
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # special case: last digit is 0
        # special case: reversed int overflow
        if str(x)[0] != "-":
            return self.reviseIfOverflow(int(str(x)[::-1]))
        else:
            return self.reviseIfOverflow(int("-" + str(self.reverse(-x))))
    def reviseIfOverflow(self, x):
        if x > self.max_int or x < self.min_int:
            return 0
        else:
            return x

def main():
    sol = Solution()
    print sol.reverse(-123) # -321
    print sol.reverse(100) # 1
    print sol.reverse(1534236469) # 0 (overflow)

if __name__ == '__main__':
    main()