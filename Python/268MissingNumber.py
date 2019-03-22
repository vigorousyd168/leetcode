class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, result = 0, 0
        for num in nums:
            result ^= num
            result ^= i
            i += 1
        result ^= i
        return result

def main():
    sol = Solution()
    print sol.missingNumber([0,1,2,3,4,5,7,8,9]) # 6
    print sol.missingNumber([0,2]) # 1
    print sol.missingNumber([0,1,3]) # 2
    print sol.missingNumber([0,1,2,3,4,5,6,7]) # 8
    print sol.missingNumber([0,1,2,3,4,5,6,7,8]) # 9

if __name__ == '__main__':
    main()