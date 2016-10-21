# 204 Count Primes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        candidates = [True] * (n/2)
        # for 2*idx + 1, but [0] for 2 instead of 1
        # candidates: [2, 3, 5, 7, ...]
        t = 0
        num = 0
        for i in xrange(1, n/2): # use xrange for better space
            # for each candidate c = 2*i+1, remove num = c*t from candidates
            # t = 3, 5, 7...
            # Can t be chosen only from candidates?
            #   No. Think of 27. 9 is removed by 3*3, then we can't remove 27 from candidates...
            if candidates[i]:
                t = 3
                num = (2*i+1)*t
                while num < n:
                    if (num-1)/2 <= n/2-1 and candidates[(num-1)/2]:
                        candidates[(num-1)/2] = False
                    t += 2
                    num = (2*i+1)*t
        result = 0
        for i in range(n/2):
            if candidates[i]:
                result += 1
        return result
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