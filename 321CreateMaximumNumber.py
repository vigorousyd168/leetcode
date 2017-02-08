# 321 Create Maximum Number
class Solution(object):
    def maxArray(self, nums, k):
        # simpler problem - played on one array
        ans = [0] * k
        last, n = -1, len(nums)
        for i in xrange(0,k):
            # pick ans[i]
            # make sure n-j >= k-i
            for j in xrange(last+1, n-k+i+1):
                # consider nums[j]
                if nums[j] > ans[i]:
                    ans[i] = nums[j]
                    last = j
        return ans
    def greater(self, nums1, i, nums2, j):
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2 and nums1[i] == nums2[j]:
            i, j = i+1, j+1
        return j == n2 or (i < n1 and nums1[i] > nums2[j])
    def merge(self, nums1, nums2, k):
        i, j = 0, 0
        ans = [0] * k
        for p in xrange(0, k):
            if self.greater(nums1,i,nums2,j):
                ans[p] = nums1[i]
                i += 1
            else:
                ans[p] = nums2[j]
                j += 1
        return ans
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        ans = [0] * k
        # pick i numbers from nums1 and k-i numbers from nums2
        for i in xrange(max(0,k-n2),min(n1,k)+1):
            candidate = self.merge(self.maxArray(nums1,i), self.maxArray(nums2,k-i), k)
            if self.greater(candidate, 0, ans, 0):
                ans = candidate
        return ans


def main():
    sol = Solution()
    print sol.maxArray([4,5,3,6,4], 3) # [5,6,4]
    print sol.maxArray([9,1,2,5,8,3], 5) # [9,2,5,8,3]
    print sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) # [9,8,6,5,3]
    print sol.maxNumber([1],[2], 2) # [2,1]
    print sol.maxNumber([6,7], [6,0,4], 5) # [6,7,6,0,4]
    print sol.maxNumber([3,9], [8,9], 3) # [9,8,9]

if __name__ == '__main__':
    main()