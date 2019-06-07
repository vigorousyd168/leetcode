class Solution {
    public int numRookCaptures(char[][] board) {
        int u = 0, v = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'R') {
                    u = i;
                    v = j;
                    break;
                }
            }
        }
        int ans = 0;
        int[][] dir = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        for (int d = 0; d < 4; d++) {
            for (int i = u+dir[d][0], j = v+dir[d][1]; 0 <= i && i < 8 && 0 <= j && j < 8; i = i+dir[d][0], j = j+dir[d][1])
            {
                if (board[i][j] != '.') {
                    if (board[i][j] == 'p') ans ++;
                    break;
                }
            }
        }
        return ans;
    }
}