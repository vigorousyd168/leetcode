class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        int n = A.length;
        int upper = A[0], lower = B[0];
        // either all A[0], or all B[0], otherwise return -1
        int upperA = 0, upperB = 1, lowerB = 0, lowerA = 1;
        for (int i = 1; i < n && (upper != 0 || lower != 0); i++) {
            if (upper != 0) {
                if (A[i] != upper && B[i] != upper) upper = 0; // give up on upper
                else {
                    if (A[i] != upper) upperA++;
                    if (B[i] != upper) upperB++;
                }
            }
            if (lower != 0) {
                if (A[i] != lower && B[i] != lower) lower = 0; // give up on lower
                else {
                    if (B[i] != lower) lowerB++;
                    if (A[i] != lower) lowerA++;
                }
            }
        }
        if (upper == 0 && lower == 0) return -1;
        int ans = n;
        if (upper != 0)
            ans = Math.min(upperA, upperB);
        if (lower != 0)
            ans = Math.min(ans, Math.min(lowerA, lowerB));
        return ans;
    }
}