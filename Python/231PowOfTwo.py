# 231 Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        bit_array = (bin(n))[3:]
        for b in bit_array:
            if b != "0":
                return False
        return True
def main():
    sol = Solution()
    print sol.isPowerOfTwo(1) # True
    print sol.isPowerOfTwo(16) # True
    print sol.isPowerOfTwo(17) # False
    print sol.isPowerOfTwo(0) # False

if __name__ == '__main__':
    main()