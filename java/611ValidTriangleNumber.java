class Solution {
    public int triangleNumber(int[] nums) {
        int count = 0, left, right;
        Arrays.sort(nums);
        for (int i = 2; i < nums.length; i++) {
            left = 0;
            right = i-1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[i]) {
                    // left, left+1... right-1 can all form a triplet with right and i
                    count += right-left;
                    right--;
                }
                else
                    left++;
            }
        }
        return count;
    }
}