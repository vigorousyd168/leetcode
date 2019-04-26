class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n < 2) return n;
        int max = nums[0], count = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > max)
            {
                nums[count++] = nums[i];
                max = nums[i];
            }
        }
        return count;
    }
}