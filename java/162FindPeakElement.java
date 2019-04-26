class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        int low = 0, high = n-1, mid = (low+high)/2;
        while (low <= high) {
            if (low == high) return low;
            mid = (low + high)/2;
            if (nums[mid] > nums[mid+1])
                high = mid;
            else
                low = mid+1;
        }
        return low;
    }
}