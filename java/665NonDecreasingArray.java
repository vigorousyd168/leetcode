class Solution {
    public boolean checkPossibility(int[] nums) {
        // if nums[i] > nums[i+1], check if nums[i] and nums[i+1]
        boolean flag = false;
        for (int i = 0; i < nums.length-1; i++) {
            if (nums[i] > nums[i+1]) {
                if (flag) return false;
                flag = true;
                // change nums[i+1] (up) or change nums[i] (down)
                if (i+2 < nums.length && nums[i] <= nums[i+2]) continue;
                if (i == nums.length-2) return true;
                if (i == 0) continue;
                if (nums[i-1] <= nums[i+1]) continue;
                return false;
            }
        }
        return true;
    }
}