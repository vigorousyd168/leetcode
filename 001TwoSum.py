# 001 TwoSum
import os
import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {} # create an empty dict
        # dict
        #   key: num
        #   value: index in nums
        for i in range(0, len(nums)): # range (0,3) is [0,1,2] - does not include 3!
            if (target - nums[i]) not in table:
                table[nums[i]] = i
            else:
                # once we find 'the partner', return
                # no need to worry about duplicate numbers
                return [table[target - nums[i]], i]
        return 'error'
def main():
    sol = Solution()
    print sol.twoSum([-1,-1,0,1,2,4],0 )
if __name__ == '__main__':
    sys.exit(main())
