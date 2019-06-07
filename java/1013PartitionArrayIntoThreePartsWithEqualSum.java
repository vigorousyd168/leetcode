class Solution {
    public boolean canThreePartsEqualSum(int[] A) {
        int sum = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
        }
        if (sum % 3 != 0) return false;
        int s = 0, hit = 0;
        for (int i = 0; i < A.length; i++) {
            s += A[i];
            if (s == sum/3) {
                if (++hit == 2) return true;
                s = 0;
            }
        }
        return false;
    }
}