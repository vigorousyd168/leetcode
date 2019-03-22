# 363 Max Sum of Rectangle No Larger Than K
import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        best = -2147483648
        for left in xrange(0, m):
            cumX = [0] * n
            for right in xrange(left, m):
                bilist, cumY = [0], 0
                for i in xrange(0, n):
                    cumX[i] += matrix[i][right]
                    cumY += cumX[i]
                    idx = bisect.bisect_left(bilist, cumY - k)
                    if idx != len(bilist):
                        candidate = bilist[idx]
                        best = max(best, cumY - candidate)
                    bisect.insort(bilist, cumY)
        return best

def main():
    sol = Solution()
    print sol.maxSumSubmatrix([[1,0,1], [0,-2,3]], 2) # 2
    print sol.maxSumSubmatrix([[1,1], [2,-3], [3,2]], 5) # 5
    print sol.maxSumSubmatrix([[1,1], [2,-3], [3,2]], 4) # 4
    print sol.maxSumSubmatrix([[1,1], [2,-3], [3,2]], 3) # 3
if __name__ == '__main__':
    main()