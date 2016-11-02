# 213 House Robber I'I
class Solution(object):
    def rob1(self, nums):
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
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 0:
            return 0
        if l <= 3:
            return max(nums)
        s = [nums[0]] + [max(nums[:2])] + [0] * (l-2)
        r = [-1] * l
        if nums[1] < nums[0]:
            r[1] = 0
        for i in range(2, l):
            if s[i-1] < s[i-2] + nums[i]:
                r[i] = i-2
                s[i] = s[i-2] + nums[i]
            else:
                s[i] = s[i-1]
                r[i] = r[i-1]
        print (s)
        print (r)
        idx = r[-1]
        zero = False
        while idx != -1:
            idx = r[idx]
            if idx == 0:
                zero = True
        print (zero)
        if r[-1] == l-3 and zero:
            return max(s[-2], self.rob1(nums[1:]))
        return s[-1]
def main():
    sol = Solution()
    print (sol.rob([2,1,1,2,])) # 4
if __name__ == '__main__':
    main()