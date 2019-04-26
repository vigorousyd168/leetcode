class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // put the number to where it is supposed to be
        List<Integer> list = new ArrayList<Integer>();
        int temp;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == i+1 || nums[i] == nums[nums[i]-1]) continue;
            temp = nums[i];
            nums[i] = nums[temp-1];
            nums[temp-1] = temp;
            i--;
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i+1)
                list.add(i+1);
        }
        return list;
    }
}

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int val;
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            val = Math.abs(nums[i]); // negate a number doesn't lose its abs value
            if (nums[val-1] > 0) nums[val-1] = -nums[val-1]; // we have val in this array
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) result.add(i+1);
        }
        return result;
    }
}