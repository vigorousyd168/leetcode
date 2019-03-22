# 303 Range Sum Query
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - (self.sums[i-1] if i >= 1 else 0)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
def main():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print (numArray.sumRange(0, 2)) # 1
    print (numArray.sumRange(2, 5)) # -1
if __name__ == '__main__':
    main()