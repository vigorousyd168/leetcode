# 204 Count Primes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        candidates = set(range(3,n,2))
        t = 0
        for i in xrange(3,n): # use xrange for better space
            if i in candidates:
                t = 2
                while i*t < n:
                    if i*t in candidates:
                        candidates.remove(i*t)
                    t += 1
        return len(candidates) + 1 # +1 for number 2
def main():
    sol = Solution()
    #print sol.countPrimes(1) # 0
    #print sol.countPrimes(3) # 1
    #print sol.countPrimes(55) # 16
    #print sol.countPrimes(56) # 16
    print sol.countPrimes(499979) # 41537
    # TLE at 499979 ~ 41537

if __name__ == '__main__':
    main()
