# 313 Super Ugly Number
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        MAX_INT = 2**31-1
        idx = [0] * k
        uglys = [1]
        val = [1] * k
        n -= 1
        # n > 0 originally => now n >= 0
        while n > 0:
            minVal = MAX_INT + 1
            for i in range(k):
                if val[i] == uglys[-1]:
                    val[i] = uglys[idx[i]] * primes[i]
                    idx[i] = idx[i] + 1
                if val[i] < minVal:
                    minVal = val[i]
            # handles overflow
            if minVal > MAX_INT:
                return -MAX_INT-1
            uglys.append(minVal)
            n -= 1
        return uglys[-1]


def main():
    sol = Solution()
    print sol.nthSuperUglyNumber(10, [2,7,13,19]) # 26
    print sol.nthSuperUglyNumber(32, [2]) # -2147483648

if __name__ == '__main__':
    main()