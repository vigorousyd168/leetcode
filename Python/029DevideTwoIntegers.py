class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1 # based on customized test case... does not make sense IMO
        neg_dividend = dividend < 0
        neg_divisor = divisor < 0
        # take abs
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        MAX_INT = 2**31-1 # special handling for Python overflow
        # construct inter
        inter = []
        powTwo = []
        base = divisor
        p = 1
        while (base <= dividend):
            inter.append(base)
            powTwo.append(p)
            base = base + base
            p = p + p
        sumInter = 0
        sumPowTwo = 0
        for k in range(len(inter)-1, -1, -1):
            if sumInter + inter[k] <= dividend:
                sumInter = sumInter + inter[k]
                sumPowTwo = sumPowTwo + powTwo[k]
        # special case
        if neg_dividend == neg_divisor:
            return sumPowTwo if sumPowTwo <= MAX_INT else MAX_INT
        else:
            return -sumPowTwo if -sumPowTwo <= MAX_INT + 1 else MAX_INT + 1

def main():
    sol = Solution()
    print sol.divide(10, 6) # 1
    print sol.divide(10, 5) # 2
    print sol.divide(0, 6) # 0
    print sol.divide(1, 6) # 0
    print sol.divide(-10, -6) # 1
    print sol.divide(-10, 6) # -1
    print sol.divide(10, -6) # -1
    print sol.divide(10, -5) # -2
    print sol.divide(0, -1) # 0
    print sol.divide(0, 0) # -1
    print sol.divide(2**31-1, 1) # 2**31-1
    print sol.divide(-2**31, 1) # -2**31
    print sol.divide(-2**31, -1) # 2**31-1
    print sol.divide(-2**31, 2) # -2**30
    print sol.divide(1004958205, -2137325331) # 0
    print sol.divide(-2**31, -2**31) # 1

if __name__ == '__main__':
    main()