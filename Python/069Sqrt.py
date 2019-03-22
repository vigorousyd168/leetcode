import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        myPow = []
        tmp = 1
        for i in range(31):
            myPow.append(tmp)
            tmp *= 2
        # myPow has [1, 2, ... , 2^30]
        result = 0
        for i in range(31):
            t = result + myPow[~i]
            if t*t < x:
                result = t
            elif t*t == x:
                return t
        return result


def main():
    sol = Solution()
    print sol.mySqrt(0) # 0
    print sol.mySqrt(1) # 1
    print sol.mySqrt(82) # 9
    print sol.mySqrt(10001) # 100
    print sol.mySqrt(2**31-1)
    print math.sqrt(2**31-1)

if __name__ == '__main__':
    main()