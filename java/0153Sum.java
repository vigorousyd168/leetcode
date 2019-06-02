class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>> ();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2; i++) {
            if (i != 0 && nums[i-1] == nums[i]) continue; // must have counted
            // nums[i] is the smallest in the triplet
            int low = i+1, high = nums.length-1, target = -nums[i];
            while (low < high) {
                if (nums[low] + nums[high] == target) {
                    result.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    while (low < high && nums[low] == nums[low+1]) low++;
                    while (low < high && nums[high] == nums[high-1]) high--;
                    low++; high--;
                }
                else if (nums[low] + nums[high] > target) high--;
                else low++;
            }
        }
        return result;
    }
}