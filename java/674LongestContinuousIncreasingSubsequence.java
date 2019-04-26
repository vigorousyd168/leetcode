class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) return 0;
        int seqLen = 1, maxLen = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) {
                seqLen++;
                if (seqLen > maxLen) maxLen = seqLen;
            }
            else seqLen = 1;
        }
        return maxLen;
    }
}