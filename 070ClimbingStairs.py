# 070 Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n
        s = [1] + [2] + [0] * (n-2)
        for i in range(2, n):
            s[i] = s[i-1] + s[i-2]
        return s[-1]
def main():
    sol = Solution()
    print (sol.climbStairs(0)) # 0
    print (sol.climbStairs(1)) # 1
    print (sol.climbStairs(2)) # 2
    print (sol.climbStairs(4)) # 5
if __name__ == '__main__':
    main()