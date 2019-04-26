class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) return 0; // absolute difference must be >= 0
        int result = 0;
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean> ();
        // stores <x, counted> where <x,y> is a pair and x <= y
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]-k)) {
                if (!map.get(nums[i]-k)) {
                    result++;
                    map.put(nums[i]-k, true);
                }
            }
            if (map.containsKey(nums[i]+k)){
                if (!map.containsKey(nums[i])) {
                    result++;
                    map.put(nums[i], true);
                }
                else {
                    if (!map.get(nums[i])) {
                        result++;
                        map.put(nums[i], true);
                    }
                }
            }
            else
                map.put(nums[i], false);
        }
        return result;
    }
}