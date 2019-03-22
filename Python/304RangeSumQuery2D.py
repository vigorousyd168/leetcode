# 304 Range Sum Query 2D - Immutable
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.isEmpty = False
        m = len(matrix)
        if m == 0:
            self.isEmpty = True
            return
        n = len(matrix[0])
        if n == 0:
            self.isEmpty = True
            return
        self.sums = []
        for i in xrange(m+1):
            self.sums.append([0] * (n+1))
        # compute sums
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] + matrix[i-1][j-1] - self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.isEmpty:
            return 0
        return self.sums[row2+1][col2+1] + self.sums[row1][col1] - self.sums[row1][col2+1] - self.sums[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

def main():
    matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]
    numMatrix = NumMatrix(matrix)
    print numMatrix.sumRegion(2, 1, 4, 3) # 8
    print numMatrix.sumRegion(1, 1, 2, 2) # 11
if __name__ == '__main__':
    main()