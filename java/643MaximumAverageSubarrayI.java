class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double avg = 0;
        for (int i = 0; i < k; i++) {
            avg += nums[i];
        }
        avg = avg/k;
        double maxAvg = avg;
        for (int i = k; i < nums.length; i++) {
            avg = avg + (double)(nums[i]-nums[i-k])/k;
            if (avg > maxAvg) maxAvg = avg;
        }
        return maxAvg;
    }
}