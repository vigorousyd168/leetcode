# 046 Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # idea 1: recursion
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return [nums]
        ret = []
        # insert nums[-1] at each position for each p (permutation of nums[:-1])
        for p in self.permute(nums[:-1]):
            # which positions? e.g. length == 2, 2 positions: 0,1
            for pos in range(length):
                # insert returns None!!!
                # pass by value/ref?
                # copy a list by value
                pp = list(p)
                pp.insert(pos,nums[-1])
                ret.append(pp)
        # need to sort...
        return sorted(ret)

def main():
    sol = Solution()
    print sol.permute([1]) # [[1]]
    print sol.permute([1,2]) # [[1,2],[2,1]]
    print sol.permute([1,2,3]) # ...Alert: the order matters!
if __name__ == '__main__':
    main()