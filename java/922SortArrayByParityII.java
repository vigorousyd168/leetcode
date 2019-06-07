class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int evenPos = 0, oddPos = 1;
        while (evenPos < A.length && oddPos < A.length) {
            // find the first misplaced number in even pos
            while (evenPos < A.length && A[evenPos] % 2 == 0) evenPos += 2;
            // find the first misplaced number in odd pos
            while (oddPos < A.length && A[oddPos] % 2 == 1) oddPos += 2;
            // swap A[evenPos] and A[oddPos]
            if (evenPos >= A.length || oddPos >= A.length) break;
            int temp = A[evenPos];
            A[evenPos] = A[oddPos];
            A[oddPos] = temp;
            evenPos += 2; oddPos += 2;
        }
        return A;
    }
}