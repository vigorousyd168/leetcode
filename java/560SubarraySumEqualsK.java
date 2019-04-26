class Solution {
    public int subarraySum(int[] nums, int k) {
        int result = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        // <preSum, numOfSuchPreArrays>
        map.put(0, 1);
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum-k))
                result += map.get(sum-k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return result;
    }
}