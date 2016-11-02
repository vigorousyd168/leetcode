# 198 House Robber
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 0:
            return 0
        if l == 1:
            return nums[0]
        m = nums[0] if nums[0] > nums[1] else nums[1]
        if l == 2:
            return m
        s = [nums[0]] + [m] + [0] * (l-2)
        for i in range(2, l):
            s[i] = s[i-1] if s[i-1] > s[i-2] + nums[i] else (s[i-2] + nums[i])
        return s[-1]
def main():
    sol = Solution()
    print (sol.rob([2,1,1,2,])) # 4
if __name__ == '__main__':
    main()