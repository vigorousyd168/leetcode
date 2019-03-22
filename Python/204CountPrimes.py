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
        c = 0
        num = 0
        for i in xrange(1, int((n/2-1)**0.5)+1): # use xrange for better space
            # for each candidate c = 2*i+1, remove num = c*t from candidates
            # t = c, c+2, c+4...
            if candidates[i]:
                c = 2*i+1
                candidates[(c*c-1)/2:n/2:c] = [False] * len(candidates[(c*c-1)/2:n/2:c])
        return sum(candidates)
def main():
    sol = Solution()
    #print sol.countPrimes(1) # 0
    #print sol.countPrimes(3) # 1
    #print sol.countPrimes(15) # 6
    #print sol.countPrimes(55) # 16
    #print sol.countPrimes(56) # 16
    print sol.countPrimes(499979) # 41537
    # TLE at 499979 ~ 41537

if __name__ == '__main__':
    main()