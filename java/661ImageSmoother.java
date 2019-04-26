class Solution {
    public int[][] imageSmoother(int[][] M) {
        int nRows = M.length;
        if (nRows == 0) return null;
        int nCols = M[0].length;
        int count, sum, u, v;
        int[][] dirs = new int[][] {{-1,-1},{-1,0},{-1,1},{0,-1},{0,0},{0,1},{1,-1},{1,0},{1,1}};
        for (int i = 0; i < nRows; i++) {
            for (int j = 0; j < nCols; j++) {
                count = 0;
                sum = 0;
                for (int k = 0; k < dirs.length; k++) {
                    u = i + dirs[k][0];
                    v = j + dirs[k][1];
                    if (u >= 0 && u < nRows && v >= 0 && v < nCols) {
                        count++;
                        sum += M[u][v] & 0xff;
                    }
                }
                M[i][j] |= sum/count << 8;
            }
        }
        for (int i = 0; i < nRows; i++) {
            for (int j = 0; j < nCols; j++) {
                M[i][j] >>= 8;
            }
        }
        return M;
    }
}