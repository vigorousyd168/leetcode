# 053 Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        maxSum = nums[0]
        s = [maxSum] + [0] * (l-1)
        for i in range(1,l):
            s[i] = (s[i-1] + nums[i]) if s[i-1] + nums[i] > nums[i] else nums[i]
            maxSum = maxSum if maxSum >= s[i] else s[i]
        return maxSum
def main():
    sol = Solution()
    print (sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
if __name__ == '__main__':
    main()