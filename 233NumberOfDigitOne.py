class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        orig = n
        result = 0
        base = 1
        while n > 0:
            d = n % 10
            result += base * (n/10)
            if d > 1:
                result += base
            elif d == 1:
                result += orig%base + 1
            n = n/10
            base = base*10
        return result

def main():
    sol = Solution()
    print sol.countDigitOne(-1) # 0
    print sol.countDigitOne(0) # 0
    print sol.countDigitOne(1) # 1
    print sol.countDigitOne(9999) # 4000
    print sol.countDigitOne(2345) # 1775
    print sol.countDigitOne(1818) # 1390


if __name__ == '__main__':
    main()