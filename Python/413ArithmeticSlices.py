# 413 Arithmetic Slices
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if l <= 2:
            return 0
        count, maxLen = 0, 0
        step = A[1] - A[0]
        for i in range(l-2):
            r = A[i+2] - A[i+1]
            if r == step:
                maxLen += 1 # maxLen is 1 when we have 3 arithmetic numbers
            else:
                step = r
                # why maxLen * (maxLen + 1) / 2 ?
                # each time we extend, we have previous sequences doubled (right shift one)
                # and then we have one more: the longest one
                count += maxLen * (maxLen + 1) / 2
                maxLen = 0
        return count + maxLen * (maxLen + 1) / 2

def main():
    sol = Solution()
    print sol.numberOfArithmeticSlices([1,2,3,4]) # 3
    print sol.numberOfArithmeticSlices([1,2,3,4,7]) # 3
    print sol.numberOfArithmeticSlices([1,2]) # 0
    print sol.numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]) # 28

if __name__ == '__main__':
    main()