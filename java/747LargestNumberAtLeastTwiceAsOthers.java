class Solution {
    public int dominantIndex(int[] nums) {
        int first = nums[0], second = -1, firstIdx = 0, secondIdx = -1;
        int n = nums.length;
        if (n == 1) return 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > first) {
                second = first;
                secondIdx = firstIdx;
                first = nums[i];
                firstIdx = i;
            }
            else if (nums[i] > second) {
                second = nums[i];
                secondIdx = i;
            }
        }
        return first >= 2*second ? firstIdx : -1;
    }
}