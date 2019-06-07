class Solution {
    public boolean validMountainArray(int[] A) {
        int n = A.length;
        if (n < 3) return false;
        boolean increasing = A[1]-A[0] > 0;
        if (!increasing) return false;
        for (int i = 1; i < n; i++) {
            if (A[i] < A[i-1])
                increasing = false;
            else if (A[i] > A[i-1]) {
                if (!increasing) return false;
            }
            else return false; // A[i] == A[i-1]
        }
        return !increasing;
    }
}