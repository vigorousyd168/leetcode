class Solution {
    public int findShortestSubArray(int[] nums) {
        int degree = 0, result = nums.length;
        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        // create map
        for (int i = 0; i < nums.length; i++) {
            // value: data [count, startPos, endPos]
            List<Integer> data;
            if (!map.containsKey(nums[i])) {
                data = new ArrayList<Integer>();
                data.add(1);
                data.add(i);
                data.add(i);
                map.put(nums[i], data);
            }
            else {
                data = map.get(nums[i]);
                data.set(0, data.get(0) + 1);
                data.remove(2);
                data.add(i);
            }
            if (data.get(0) > degree)
                degree = data.get(0);
        }
        // find smallest length
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            List<Integer> data = entry.getValue();
            if (data.get(0) == degree) {
                if (data.get(2) - data.get(1) + 1 <= result)
                    result = data.get(2) - data.get(1)  + 1;
            }
        }
        return result;
    }
}