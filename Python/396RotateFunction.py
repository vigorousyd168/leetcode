# 396 Rotate Function
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        F = [0]
        s, n = 0, len(A)
        for i in xrange(n):
            F[0] = F[0] + i*A[i]
            s += A[i]
        for i in xrange(1, n):
            F.append(F[-1] + s - n*A[n-i])
        return max(F)

def main():
    sol = Solution()
    print sol.maxRotateFunction([4,3,2,6]) # 26
    print sol.maxRotateFunction([]) # 0
    print sol.maxRotateFunction([1,1]) # 1

if __name__ == '__main__':
    main()