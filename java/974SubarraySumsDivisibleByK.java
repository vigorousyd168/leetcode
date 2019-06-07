class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int n = A.length, sum = 0, ans = 0;
        int[] preSum = new int[n+1];
        for (int i = 0; i < n; i++) {
            sum += A[i];
            preSum[i+1] = sum;
        }
        // preSum[i+1] is sum of A[0]..A[i]
        int[] count = new int[K];
        for (int s : preSum) {
            count[(s % K + K)%K]++; // note that in Java % could give netgative result
        }
        for (int c : count)
            ans += c * (c-1) / 2;
        return ans;
    }
}