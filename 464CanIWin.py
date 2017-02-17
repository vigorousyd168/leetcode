# 464 Can I Win
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def canWin(nums, desired, d):
            """
            :type nums: list
            :type desired: int
            :type d: dict
            :rtype: bool
            """
            key = str(nums)
            if key in d:
                return d[key]
            if nums[-1] >= desired:
                d[key] = True
                return True
            for i in xrange(len(nums)):
                if not canWin(nums[:i] + nums[i+1:], desired - nums[i], d):
                    d[key] = True
                    return True
            d[key] = False
            return False

        maxSum = maxChoosableInteger * (maxChoosableInteger+1) / 2
        if maxSum < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        d = {}
        return canWin(range(1, maxChoosableInteger+1), desiredTotal, d)

def main():
    sol = Solution()
    print sol.canIWin(10, 11) # False
    print sol.canIWin(4, 3) # True 
    print sol.canIWin(4, 5) # False
    print sol.canIWin(4, 6) # True
if __name__ == '__main__':
    main()