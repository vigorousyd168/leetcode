class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in xrange(l>>1):
            for j in xrange(l-(l>>1)):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                  matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

        print matrix
def main():
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print mat
    # but how to operate "in place" in Python?
    sol.rotate(mat)

if __name__ == '__main__':
    main()