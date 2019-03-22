# 202 Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n = n if n > 0 else -n
        numbers = set() # a set
        while 1:
            if n in numbers:
                return False
            numbers.add(n)
            if n == 1:
                return True
            digits = [int(s) for s in str(n)]
            n = 0
            for d in digits:
                n += d*d

def main():
    sol = Solution()
    print sol.isHappy(1) # True
    print sol.isHappy(3) # False
    print sol.isHappy(19) # True
    print sol.isHappy(5) # False

if __name__ == '__main__':
    main()
        