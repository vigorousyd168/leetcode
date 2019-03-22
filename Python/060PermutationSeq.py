# 60 Permutation Sequence
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"
        digits = range(1, n+1)
        remaining = digits
        # note: digits[k] = k+1
        result = ""
        fac = []
        temp = 1
        for i in digits[:-1]:
            temp = temp * i
            fac.append(temp)
        # fac is the list of 1!, 2!,..., (n-1)!, fac[k] = (k+1)!
        for i in range(n):
            d = (k-1) / fac[~i] # make sure index is in range
            print i,d,k,remaining
            result = result + str(remaining[d])
            remaining.remove(remaining[d])
            k -= d * fac[~i]
            # termination
            if k == 1:
                return result + "".join([str(x) for x in remaining])


def main():
    sol = Solution()
    print sol.getPermutation(1,1) # "1"
    print sol.getPermutation(3,5) # "312"
    print sol.getPermutation(3,4) # "231"
    print sol.getPermutation(4,13) # "3124"

if __name__ == '__main__':
    main()