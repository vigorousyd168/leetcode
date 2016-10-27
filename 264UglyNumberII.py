# 264 Ugly Number II
import time
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1,2,3,4,5]
        if n <= 5:
            return uglys[n-1]
        idx2, idx3, idx5 = 2, 1, 1
        n = n - 5
        while n > 0:
            uglys.append(min(uglys[idx2]*2, uglys[idx3]*3, uglys[idx5]*5))
            if uglys[-1] == uglys[idx2]*2:
                idx2 += 1
            if uglys[-1] == uglys[idx3]*3:
                idx3 += 1
            if uglys[-1] == uglys[idx5]*5:
                idx5 += 1
            n -= 1
        return uglys[-1]

def main():
    sol = Solution()
    start_time = time.clock()
    print sol.nthUglyNumber(6) # 6
    print sol.nthUglyNumber(7) # 8
    print sol.nthUglyNumber(199) # 16000
    print sol.nthUglyNumber(287) # 69120
    print sol.nthUglyNumber(1000) # 51200000
    print("--- %s seconds ---" % (time.clock() - start_time))

if __name__ == '__main__':
    main()