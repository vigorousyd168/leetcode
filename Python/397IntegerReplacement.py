# 397 Integer Replacement
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0: consume
        # 1: +=1 if next is 1 and n > 3, else -=1
        res = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            else:
                if (n >> 1) & 1 and n > 3:
                    n = n + 1
                else:
                    n = n - 1
            res += 1
        return res

def main():
    sol = Solution()
    print sol.integerReplacement(1) # 0
    print sol.integerReplacement(3) # 2
    print sol.integerReplacement(7) # 4
    print sol.integerReplacement(8) # 3
    print sol.integerReplacement(20) # 5
    print sol.integerReplacement(119) # 9
    print sol.integerReplacement(178) # 10
    print sol.integerReplacement(48) # 6
    print sol.integerReplacement(380) # 10
    print sol.integerReplacement(760) # 11
    print sol.integerReplacement(763) # 12

if __name__ == '__main__':
    main()