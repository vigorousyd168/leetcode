import java.util.ArrayList;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] err = {-3,-3};
        int[] add = {-1,-1};
        ArrayList<Integer> a = new ArrayList();
        for (int k = 0; k < nums.length; k++){
            a.add(nums[k]);
        }
        Collections.sort(a);
        // sorting? it loses info about original indices!!!
        // but we can get them in one pass: O(n)
        for (int i = 0; i < a.size(); i++){
            for (int j = i+1; j < a.size(); j++){
                if ((a.get(i) + a.get(j)) == target){
                    add[0] = a.get(i);
                    add[1] = a.get(j);
                    return findIdx(nums, add);
                }
                else if ((a.get(i) + a.get(j)) > target){
                    break;
                }
                // else, less than target, continue
            }
        }
        return err; //error
    }
    
    private int[] findIdx(int[] nums, int[] add){
        // nums is not sorted now!!!
        int[] ans = {-2,-2};
        for (int i = 0; i < nums.length; i++){
            if (ans[0] == -2){ // ans[0] not found yet
                if (nums[i] == add[0]){
                    ans[0] = i; // consider duplicate numbers
                    continue;
                }
            }
            if (ans[1] == -2){ // ans[1] not found yet
                if (nums[i] == add[1]){
                    ans[1] = i; // consider duplicate numbers
                    continue;
                }
            }
        }
        return ans;
    } 
}