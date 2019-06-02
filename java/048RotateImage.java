class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // [i][j] -> [j][n-1-i]
        // [j][n-1-i] -> [n-1-i][n-1-j]
        // [n-1-i][n-1-j] -> [n-1-j][i]
        // [n-1-j][i] -> [i][j]
        int temp;
        for (int i = 0; i < n/2; i++) {
            for (int j = 0; j < (n+1)/2; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = temp;
            }
        }
    }
}