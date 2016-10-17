class Solution(object):
    def findKthElm(self, nums1, nums2, k, m, n):
        # make sure m <= n
        if m > n:
            return self.findKthElm(nums2, nums1, k, n, m)
        # trivial cases
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]
        i = m if m < k/2 else k/2
        j = n if n < k/2 else k/2
        if nums1[i-1] < nums2[j-1]:
            # throw away left part of nums1
            return self.findKthElm(nums1[i:], nums2, k - i, m - i, n)
            # throw away left part of nums2
        else:
            return self.findKthElm(nums1, nums2[j:], k - j, m, n - j)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        k1 = (m+n+1)/2
        k2 = (m+n+2)/2
        # handles both even and odd
        return (self.findKthElm(nums1, nums2, k1, m, n) + self.findKthElm(nums1, nums2, k2, m, n))/2.0

def main():
    sol = Solution()
    print sol.findMedianSortedArrays([1], [1,1,1]) # 1.0
    print sol.findMedianSortedArrays([1,3], [2]) # 2

if __name__ == '__main__':
    main()