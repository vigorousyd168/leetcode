class Solution {
    public boolean isIdealPermutation(int[] A) {
        // look at A[i] locally
        // we only allow local inversion
        // A[i] == i+1, A[i+1] == i
        int i = 0;
        while (i < A.length) {
            if (A[i] == i+1)
            {
                if (i+1 < A.length && A[i+1] != i) return false;
                i += 2;
            }
            else if (A[i] != i) {
                return false;
            }
            else {
                i++;
            }
        }
        return true;
    }
}