class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int m = A.length, n = A[0].length;
        for (int i = 0; i < m; i++) {
            int left = 0, right = n-1;
            while (left < right) {
                if (A[i][left] == A[i][right]) {
                    A[i][left] = 1 - A[i][left];
                    A[i][right] = 1 - A[i][right];
                }
                left++; right--;
            }
            if (left == right)
                A[i][left] = 1 - A[i][left];
        }
        return A;
    }
}