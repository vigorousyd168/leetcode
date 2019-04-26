class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<Integer> ();
        int nrows = matrix.length;
        if (nrows == 0) return res;
        int ncols = matrix[0].length;

        int dir = ncols == 1 ? 1 : 0;
        // 0: right, 1: down, 2: left, 3: up
        int right = ncols-1, down = nrows-1, left = ncols-1, up = nrows-1;
        int idx = 0, i = 0, j = 0, counter = 0;
        if (ncols == 1) {
            counter = down+1;
            down--; right--;
            i--;
        }
        else {
            counter = right+1;
            right--; up--;
            j--;
        }
        while (idx < nrows*ncols) {
            switch (dir){
                case 0:
                    j++;
                    counter--;
                    if (counter == 0) {
                        dir = 1;
                        counter = down;
                        down -= 2;
                    }
                    break;
                case 1:
                    i++;
                    counter--;
                    if (counter == 0) {
                        dir = 2;
                        counter = left;
                        left -= 2;
                    }
                    break;
                case 2:
                    j--;
                    counter--;
                    if (counter == 0) {
                        dir = 3;
                        counter = up;
                        up -= 2;
                    }
                    break;
                case 3:
                    i--;
                    counter--;
                    if (counter == 0) {
                        dir = 0;
                        counter = right;
                        right -= 2;
                    }
                default:
                    break;
            
            }
            //System.out.println("i: " + i + "; j: " + j + "; c: " + counter);
            res.add(matrix[i][j]);
            idx++;
        }
        return res;
    }
}