# 263 Ugly Number
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        # 1 is included
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1

def main():
    sol = Solution()
    print sol.isUgly(-1) # False
    print sol.isUgly(0) # False
    print sol.isUgly(1) # True
    print sol.isUgly(10) # True
    print sol.isUgly(14) # False

if __name__ == '__main__':
    main()