class Solution {
    public boolean isMonotonic(int[] A) {
        int dir = 0; // 0: unknown; 1: up; 2: down
        for (int i = 1; i < A.length; i++) {
            if (A[i] > A[i-1]) {
                if (dir == 2) return false;
                dir = 1;
            }
            else if (A[i] < A[i-1]) {
                if (dir == 1) return false;
                dir = 2;
            }
        }
        return true;
    }
}