class Solution {
    public int[] constructArray(int n, int k) {
        // 1, n, 2, n-1, 3, n-2...
        int[] result = new int[n];
        for (int i = 0; i < k; i++) {
            result[i] = i % 2 == 0 ? i/2+1 : n-i/2;
        }
        for (int i = k; i < n; i++) {
            if (k % 2 == 1) {
                result[i] = k/2+2 + i-k;
            }
            else {
                result[i] = n-k/2 + k-i;
            }
        }
        return result;
    }
}