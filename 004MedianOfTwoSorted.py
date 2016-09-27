import math

class Solution(object):
    odd = False;

    def findFirstIdx(self, pivot, nums2, n): # binary search
        if n == 1:
            if pivot > nums2[0]: # nothing in nums2 is > pivot
                return 1
            else:
                return 0
        if n == 0:
            return 0
        if nums2[0] > pivot:
            return 0
        
        i = int(math.floor(n/2))
        if nums2[i] <= pivot:
            return i + self.findFirstIdx(pivot, nums2[i:], n-i)
        else:
            return self.findFirstIdx(pivot, nums2[0:i], i)
    def resolveTrivial(self, nums1, nums2, k, m, n):
        print ("resolving trivial")
        print (nums1, nums2, k, m, n)
        nums = nums1 + nums2
        s = sorted(nums)
        # check if total count is odd
        if self.odd:
            return s[k-1]
        return float(s[k-1] + s[k])/2
    def findKthEleInTwoArrays(self, nums1, nums2, k, m, n):
        # make sure m >= n
        print ("finding ", k, "th element")
        print (nums1, nums2, k, m, n)
        if n > m:
            return self.findKthEleInTwoArrays(nums2, nums1, k, n, m)
        if m < 3:
            return self.resolveTrivial(nums1, nums2, k, m, n)
        # reduce
        # part 1: remove the smaller floor((m-1)/2) elements from m
        idx1 = int(math.floor((m-1) / 2))
        pivot = nums1[idx1]
    
        # part 2: find the first elem in nums2 that is > nums1(floor((m-1)/2))
        # or - find how many elems in nums2 <= pivot
        idx2 = self.findFirstIdx(pivot, nums2, n) # binary search
        
        # part 3:
        # now there are (idx1 + idx2) numbers <= pivot
        print ("idx1", idx1, "idx2", idx2)
        if (idx1 + idx2) == (k-1):
            if self.odd:
                return pivot
            else:
                left = pivot
                right = sorted(nums1[idx1:]+nums2[idx2:])[1]
                print (left, right)
                return float(left+right)/2

        elif (idx1 + idx2) < (k-1):
            # search on the right
            return self.findKthEleInTwoArrays(nums1[idx1:], nums2[idx2:], k-idx1-idx2, m-idx1, n-idx2)
        elif (idx1 + idx2) > (k-1):
            # search on the left
            if n == 0:
                return self.findKthEleInTwoArrays(nums1[0:idx1+1], nums2[0:0], k, idx1+1, 0)
            return self.findKthEleInTwoArrays(nums1[0:idx1+1], nums2[0:idx2], k, idx1+1, idx2)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        self.odd = (m+n) % 2 != 0
        k = (m+n+1)/2
        return self.findKthEleInTwoArrays(nums1, nums2, k, m, n)

def main():
    sol = Solution()
    print sol.findMedianSortedArrays([1], [1,1,1])

if __name__ == '__main__':
    main()