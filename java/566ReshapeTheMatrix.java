class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        if (nums.length == 0) return nums;
        int oldR = nums.length, oldC = nums[0].length;
        if (oldR * oldC != r * c) return nums;
        int[][] result = new int[r][c];
        int k = 0;
        for (int i = 0; i < oldR; i++) {
            for (int j = 0; j < oldC; j++) {
                result[k/c][k%c] = nums[i][j];
                k++;
            }
        }
        return result;
    }
}