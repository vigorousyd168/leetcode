class Solution {
    public int[] sortedSquares(int[] A) {
        int n = A.length;
        int i = 0, j = n-1, k = n-1;
        int[] B = new int[n];
        while (i <= j) {
            if (Math.abs(A[i]) < Math.abs(A[j]))
                B[k--] = A[j--];
            else
                B[k--] = A[i++];
        }
        for (int u = 0; u < n; u++) {
            B[u] = B[u] * B[u];
        }
        return B;
    }
}