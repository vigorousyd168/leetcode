# 221 Maximum Square
class Solution(object):
    def newMatrix(self, m, n):
        res = []
        for i in range(m):
            res.append([0] * n)
        return res

    def maximalSquare2(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        left = self.newMatrix(m, n)
        top = self.newMatrix(m, n)
        sq = self.newMatrix(m, n)
        for i in xrange(m):
            for j in xrange(n):
                if int(matrix[i][j]) == 1:
                    left[i][j] = left[i][j-1] + 1 if j > 0 else 1
                    top[i][j] = top[i-1][j] + 1 if i > 0 else 1
                else:
                    left[i][j] = 0
                    top[i][j] = 0
        res = 0
        # handle first row and first col
        for j in xrange(n):
            sq[0][j] = int(matrix[0][j])
            if sq[0][j] > res:
                res = sq[0][j]
        for i in xrange(1, m):
            sq[i][0] = int(matrix[i][0])
            if sq[i][0] > res:
                res = sq[i][0]
        for i in xrange(1,m):
            for j in xrange(1,n):
                pre = sq[i-1][j-1]
                if pre > 0 and int(matrix[i][j]) == 1:
                    sq[i][j] = min(left[i][j],top[i][j],pre+1) #
                else:
                    sq[i][j] = int(matrix[i][j])
                if sq[i][j] > res:
                    res = sq[i][j]
        return res*res
    def maximalSquare(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        dp = [0] * n
        pre = [0] * n
        for j in xrange(n):
            pre[j] = 1 if matrix[0][j] == '1' else 0
        res = max(pre)
        for i in xrange(1,m):
            dp[0] = 1 if matrix[i][0] == '1' else 0
            for j in xrange(1,n):
                dp[j] = min(pre[j-1],dp[j-1],pre[j])+1 if matrix[i][j] == '1' else 0
            for j in xrange(n):
                pre[j] = dp[j]
                if dp[j] > res:
                    res = dp[j]
        return res*res


def main():
    sol = Solution()
    print sol.maximalSquare([[1]]) # 1
    print sol.maximalSquare(["10","10"]) # 1
    print sol.maximalSquare(["10100","10111","11111","10010"]) # 4
    print sol.maximalSquare(["1010","1011","1011","1111"]) # 4
    for m in ["0110111111111111110","1011111111111111111","1101111111110111111","1111111111111011111","1111111111111101111","1110111011111111101","1011111111111101111","1111111111111110110","0011111111111110111","1101111111011111111","1111111110111111111","0110111011111111111","1111011111111101111","1111111111111111111","1111111111111111111","1111111111111111101","1111111101101101111","1111110111111110111"]:
        print m
    print sol.maximalSquare(["0110111111111111110","1011111111111111111","1101111111110111111","1111111111111011111","1111111111111101111","1110111011111111101","1011111111111101111","1111111111111110110","0011111111111110111","1101111111011111111","1111111110111111111","0110111011111111111","1111011111111101111","1111111111111111111","1111111111111111111","1111111111111111101","1111111101101101111","1111110111111110111"]) # 25

if __name__ == '__main__':
    main()

