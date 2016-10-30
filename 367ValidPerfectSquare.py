# 367 Valid Perfect Square
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        powerOfTwo = []
        base = 1
        while base*base <= num:
            powerOfTwo.append(base)
            base *= 2
        root = base/2
        if root*root == num:
            return True
        for i in range(len(powerOfTwo)-2, -1, -1):
            sq = (root+powerOfTwo[i]) * (root+powerOfTwo[i])
            if sq == num:
                return True
            elif sq < num:
                root += powerOfTwo[i]
        return False
    def isPerfectSquare2(self, num):
        # binary search
        low, high = 1, num
        while low <= high:
            mid = low + (high - low)/2
            sq = mid * mid
            if sq > num:
                high = mid - 1
            elif sq < num:
                low = mid + 1
            else:
                return True
        return False
    def isPerfectSquare3(self, num):
        # Newton method
        if num == 1:
            return 0
        t = num/2 # or, init t = num, and remove the num == 1 check
        while t * t > num:
            t = (t + num/t)/2
        return t*t == num

def main():
    sol = Solution()
    #print sol.isPerfectSquare(0) # True
    print sol.isPerfectSquare(1) # True
    print sol.isPerfectSquare(4) # True
    print sol.isPerfectSquare(9) # True
    print sol.isPerfectSquare(6) # False
    print sol.isPerfectSquare(2**30) # True


if __name__ == '__main__':
    main()