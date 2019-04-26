class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0, n = nums.length;
        int[] sums = new int[n];
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            sums[i] = sum;
        }
        int leftSum = 0, rightSum = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0) leftSum = sums[i-1];
            rightSum = sums[n-1] - sums[i];
            if (leftSum == rightSum) return i;
        }
        return -1;
    }
}