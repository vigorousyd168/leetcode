class Solution {
    public int searchInsert(int[] nums, int target) {
        // idea: binary search
        // consider duplicates
        int i = 0, j = nums.length-1, idx;
        while (i <= j) {
            idx = (i + j)/2;
            if (nums[idx] == target) return idx;
            if (nums[idx] > target) j = idx - 1;
            else i = idx + 1;
        }
        return i;
    }
}