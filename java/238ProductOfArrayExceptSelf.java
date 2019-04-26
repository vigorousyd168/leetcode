class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = Arrays.copyOf(nums, nums.length);
        for (int i = 0; i < nums.length; i++) {
            res[i] = 1;
        }
        int temp = 1;
        for (int i = 0; i < nums.length; i++) {
            res[i] *= temp;
            temp *= nums[i];
        }
        temp = 1;
        for (int i = nums.length-1; i >= 0; i--) {
            res[i] *= temp;
            temp *= nums[i];
        }
        return res;
    }
}