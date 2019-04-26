class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int[] copy = nums.clone();
        Arrays.sort(copy);
        int start, end;
        for (start = 0; start < nums.length; start++) {
            if (copy[start] != nums[start]) break;
        }
        for (end = nums.length-1; end >= 0; end--) {
            if (copy[end] != nums[end]) break;
        }
        return start < end ? end-start+1 : 0;
    }
}