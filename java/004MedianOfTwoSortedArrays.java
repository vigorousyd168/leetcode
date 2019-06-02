class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // nums1 0,1,2,...,i-1  | i,i+1,...,m
        // nums2 0,1,2,...,j-1  | j,j+1,...,n
        if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        int m = nums1.length, n = nums2.length;
        // (1) # numbers left == # numbers right: i+j == m-i + n-j
        // (2) nums2[j-1] <= nums1[i]; nums1[i-1] <= nums2[j]
        int low = 0, high = m;
        while (low <= high) {
            int i = (low+high)/2;
            int j = (m+n+1)/2-i;
            if (i > low && nums1[i-1] > nums2[j]) {
                high = i-1;
            }
            else if (i < high && nums1[i] < nums2[j-1]) {
                low = i+1;
            }
            else {
                int maxLeft, minRight;
                if (i == 0) maxLeft = nums2[j-1];
                else if (j == 0) maxLeft = nums1[i-1];
                else maxLeft = Math.max(nums1[i-1], nums2[j-1]);
                
                if ((m+n) % 2 == 1) return maxLeft;
                
                if (i >= m) minRight = nums2[j];
                else if (j >= n) minRight = nums1[i];
                else minRight = Math.min(nums1[i], nums2[j]);
                
                return (maxLeft+minRight)/2.0;
            }
        }
        return 0.0;
    }
}