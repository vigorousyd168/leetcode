# 152 Maximum Product Subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        maxGlobal = maxSoFar = minSoFar = nums[0]
        for i in range(1,l):
            # simultaneous update
            maxSoFar, minSoFar = max(maxSoFar*nums[i],minSoFar*nums[i],nums[i]), min(maxSoFar*nums[i],minSoFar*nums[i],nums[i])
            if maxSoFar > maxGlobal:
                maxGlobal = maxSoFar
        return maxGlobal

def main():
    sol = Solution()
    print sol.maxProduct([2,3,-2,4]) # 6
    print sol.maxProduct([]) # 0
    print sol.maxProduct([1]) # 1
    print sol.maxProduct([-1]) # -1
    print sol.maxProduct([1,-1]) # 1
    print sol.maxProduct([-1,-1]) # 1
    print sol.maxProduct([0,2]) # 2
    print sol.maxProduct([-2,0,-1]) # 0
    print sol.maxProduct([0,-2,4,2]) # 8
    print sol.maxProduct([2,-5,-2,-4,3]) # 24
if __name__ == '__main__':
    main()