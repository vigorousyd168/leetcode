# 416 Partition Equal Subset Sum
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        t = s/2
        sums = set()
        if t in sums:
            return True
        for i in xrange(len(nums)):
            newSums = set([nums[i]])
            for x in sums:
                if x + nums[i] not in sums and x + nums[i] <= t:
                    newSums.add(x + nums[i])
            if t in newSums:
                return True
            sums = sums | newSums
        return False

def main():
    sol = Solution()
    print sol.canPartition([1,2,5]) # False
    print sol.canPartition([10,9,2,5,3,7,101,18]) # False
    print sol.canPartition([1,5,11,5]) # True
    print sol.canPartition([1]) # False
if __name__ == '__main__':
    main()