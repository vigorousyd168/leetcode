class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<String> ();
        String temp;
        if (nums.length == 0) return result;
        int low = nums[0], high = nums[0]-1;
        for (int i = 0; i < nums.length; i++)
        {
            if (nums[i] == high+1) high++;
            else {
                if (low == high)
                    result.add(low + "");
                else
                    result.add(low + "->" + high);
                low = high = nums[i];
            }
        }
        // last range
        if (low == high)
            result.add(low + "");
        else
            result.add(low + "->" + high);
        return result;
    }
}