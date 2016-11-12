# 376 Wiggle Subsequence
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return l
        res = 1
        seq = [nums[0]]
        start = 1
        while nums[start] == nums[start-1]:
            start += 1
            if start > l - 1:
                return res
        up = True if nums[start] > nums[start-1] else False # up: last move was up
        seq.append(nums[start])
        res += 1
        for i in xrange(start+1, l):
            if (up and nums[i] < nums[i-1]) or (not up and nums[i] > nums[i-1]):
                seq.append(nums[i])
                res += 1
                up = not up
        return res
    def wiggleMaxLength1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return l
        up = [1] + [0] * (l-1) # max length of wiggle subseq with last element going up
        down = [1] + [0] * (l-1) # max length of wiggle subseq with last element going down
        upTop, downBottom = nums[0], nums[0]
        for i in xrange(1, l):
            newUpTop, newDownBottom = upTop, downBottom
            if nums[i] < upTop:
                down[i] = up[i-1] + 1
                newDownBottom = nums[i]
            else:
                down[i] = down[i-1]
                if nums[i] > upTop:
                    newUpTop = nums[i]
            if nums[i] > downBottom:
                up[i] = down[i-1] + 1
                newUpTop = nums[i]
            else:
                up[i] = up[i-1]
                if nums[i] < downBottom:
                    newDownBottom = nums[i]
            upTop, downBottom = newUpTop, newDownBottom
        return max(up[-1], down[-1])

def main():
    sol = Solution()
    print sol.wiggleMaxLength([1]) # 1
    print sol.wiggleMaxLength([1,1]) # 1
    print sol.wiggleMaxLength([1,2]) # 2
    print sol.wiggleMaxLength([1,2,3,4]) # 2
    print sol.wiggleMaxLength([1,7,4,9,2,5]) # 6
    print sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) # 7
    print sol.wiggleMaxLength([1,3,5,4,5,4]) # 5
if __name__ == '__main__':
    main()