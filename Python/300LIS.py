# 300 Longest Increasing Subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        M = [0]* (n+1)
        for i in xrange(n):
            lo = 1
            hi = l
            while lo <= hi:
                mid = (lo + hi + 1)/2
                if nums[M[mid]] < nums[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            newL = lo
            M[newL] = i
            if newL > l:
                l = newL
        return l

def main():
    sol = Solution()
    print sol.lengthOfLIS([10,9,2,5,3,7,101,18]) # 4
    print sol.lengthOfLIS([]) # 0
    print sol.lengthOfLIS([0]) # 1
if __name__ == '__main__':
    main()