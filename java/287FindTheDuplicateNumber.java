class Solution {
    public int findDuplicate(int[] nums) {
        int pos;
        for (int i = 0; i < nums.length; i++) {
            pos = Math.abs(nums[i])-1;
            if (nums[pos] < 0) return pos+1;
            nums[pos] = -nums[pos];
        }
        return 0;
    }
}