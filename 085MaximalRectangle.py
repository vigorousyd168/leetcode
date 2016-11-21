# 085 Maximal Rectangle
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        height = [0] * n
        left = [0] * n
        right = [n] * n
        res = 0
        for i in xrange(m):
            curr_left, curr_right = 0, n # left inclusive, right exclusive
            for j in xrange(n):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
                if matrix[i][j] == '1':
                    left[j] = curr_left if curr_left >= left[j] else left[j]
                else:
                    left[j], curr_left = 0, j + 1
            for j in xrange(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = curr_right if curr_right <= right[j] else right[j]
                else:
                    right[j], curr_right = n, j
                if (right[j] - left[j]) * height[j] > res:
                    res = (right[j] - left[j]) * height[j]
        return res
def main():
    sol = Solution()
    print sol.maximalRectangle(["10100","10111","11111","10010"]) # 6
    print sol.maximalRectangle(["1"]) # 1
    print sol.maximalRectangle(["0001","0011","0111","1111"]) # 6
if __name__ == '__main__':
    main()