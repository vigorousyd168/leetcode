class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        int[] ans = new int[queries.length];
        int sum = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 == 0) sum += A[i];
        }
        for (int i = 0; i < queries.length; i++) {
            int addVal = queries[i][0], index = queries[i][1];
            int oldVal = A[index];
            int newVal = oldVal + addVal;
            if (oldVal % 2 == 0) {
                if (addVal % 2 == 0)
                    sum += addVal;
                else
                    sum -= oldVal;
            }
            else {
                if (addVal % 2 != 0) // caution: in Java -5 % 2 = -1
                    sum += newVal;
                // otherwise sum has no change
            }
            A[index] = newVal;
            ans[i] = sum;
        }
        return ans;
    }
}