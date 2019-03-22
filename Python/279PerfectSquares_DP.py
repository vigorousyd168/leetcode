# 279 Perfect Squares
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        numSq = [0]
        MAX_INT = 2**31-1
        for i in range(1,n+1):
            j = 1
            minNum = MAX_INT
            while j*j <= i:
                minNum = min(minNum, numSq[i-j*j] + 1) # 1 for a square (j*j)
                j += 1
            numSq.append(minNum)
        return numSq[-1]
def main():
    sol = Solution()
    print sol.numSquares(1) # 1
    print sol.numSquares(2) # 2
    print sol.numSquares(7) # 4
    print sol.numSquares(12) # 3
    print sol.numSquares(16) # 1
    print sol.numSquares(20) # 2
    print sol.numSquares(21) # 3
    print sol.numSquares(50000) # 2

if __name__ == '__main__':
    main()