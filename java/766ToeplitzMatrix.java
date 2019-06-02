class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) return true;
        int n = matrix[0].length;
        int u,v;
        for (int i = 0; i < m; i++) {
            // start from [i, 0]
            u = i; v = 0;
            while (u+1 < m && v+1 < n) {
                if (matrix[u+1][v+1] != matrix[u][v]) return false;
                u++; v++;
            }
        }
        for (int i = 1; i < n; i++) {
            // start from [0, i]
            u = 0; v = i;
            while (u+1 < m && v+1 < n) {
                if (matrix[u+1][v+1] != matrix[u][v]) return false;
                u++; v++;
            }
        }
        return true;
    }
}