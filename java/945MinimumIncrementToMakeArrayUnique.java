class Solution {
    public int minIncrementForUnique(int[] A) {
        // 0 <= A[i] < 40000, 0 <= A.length <= 40000
        // worst case we have to increment a number to 39999 + 39999
        int MAX_N = 40000, MAX_VALUE = 40000;
        int[] count = new int[MAX_N + MAX_VALUE];
        for (int a : A) count[a] += 1;
        int ans = 0, pending = 0;
        for (int a = 0; a < MAX_N + MAX_VALUE; a++) {
            if (count[a] >= 2) {
                pending += count[a]-1;
                // if in the final result, we increment u to v, we can do it as
                // ans -= u-0 when we meet u, ans += v-0 when we meet v
                ans -= a * (count[a]-1);
            }
            else if (pending > 0 && count[a] == 0) {
                pending--;
                ans += a;
            }
        }
        return ans;
    }
}