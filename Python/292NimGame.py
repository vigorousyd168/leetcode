class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 4k+1, 4k+2, 4k+3
        return (n > 0) and (n % 4 != 0)

def main():
    sol = Solution()
    print sol.canWinNim(4)
if __name__ == '__main__':
    main()