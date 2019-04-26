class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] s = new int[n];
        // s[] is the max sum of contiguous subarrays ending at i
        int maxSum = s[0] = nums[0];
        for (int i = 1; i < n; i++) {
            s[i] = s[i-1] + nums[i] > nums[i] ? s[i-1] + nums[i] : nums[i];
            if (s[i] > maxSum) maxSum = s[i];
        }
        return maxSum;
    }
}