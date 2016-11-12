# 374 Guess Number Higher or Lower I

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

number = 7
def guess(num):
    if num < number:
        return 1
    elif num > number:
        return -1
    else:
        return 0
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            # guess is mid
            mid = (lo + hi)/2
            r = guess(mid)
            if r == -1:
                hi = mid - 1
            elif r == 1:
                lo = mid + 1
            else:
                return mid
def main():
    sol = Solution()
    print sol.guessNumber(10) # return 6
if __name__ == '__main__':
    main()
