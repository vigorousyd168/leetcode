class Solution {
    public int movesToChessboard(int[][] board) {
        // validity: four corners are 1111, 1100, 1010, 0101, 0000, 0011, 1001, 0110
        // or, NW xor NE == SW xor SE
        int N = board.length;
        int NW, NE, SW, SE, ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                NW = board[0][0];
                NE = board[0][j];
                SW = board[i][0];
                SE = board[i][j];
                if ((NW ^ NE) != (SW ^ SE)) return -1; // add brackets! priority of ^ is lower than !=
            }
        }
        // swap rows to make the first column good
        // look at board[][0]
        int ones = 0, onesAtEvenPos = 0, onesAtOddPos = 0;
        for (int i = 0; i < N; i++) {
            if (board[i][0] == 1) {
                ones++;
                if (i % 2 == 0) onesAtEvenPos++;
                else onesAtOddPos++;
            }
        }
        if (N % 2 == 0) {
            if (ones != N/2) return -1;
            ans += Math.min (N/2 - onesAtEvenPos, N/2 - onesAtOddPos);
        }
        else {
            if (ones == (N+1)/2) ans += (N+1)/2 - onesAtEvenPos;
            else if (ones == (N-1)/2) ans += (N-1)/2 - onesAtOddPos;
            else return -1;
        }
        // swap columns to make the first row good
        // look at board[0][]
        ones = 0; onesAtEvenPos = 0; onesAtOddPos = 0;
        for (int j = 0; j < N; j++) {
            if (board[0][j] == 1) {
                ones++;
                if (j % 2 == 0) onesAtEvenPos++;
                else onesAtOddPos++;
            }
        }
        if (N % 2 == 0) {
            if (ones != N/2) return -1;
            ans += Math.min (N/2 - onesAtEvenPos, N/2 - onesAtOddPos);
        }
        else {
            if (ones == (N+1)/2) ans += (N+1)/2 - onesAtEvenPos;
            else if (ones == (N-1)/2) ans += (N-1)/2 - onesAtOddPos;
            else return -1;
        }
        return ans; 
    }
}