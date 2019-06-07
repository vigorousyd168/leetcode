class Solution {
    public int minFlipsMonoIncr(String S) {
        int cOnesLeft = 0, n = S.length();
        int ans = n;
        int[] cZerosRight = new int[n];
        cZerosRight[n-1] = S.charAt(n-1) == '0' ? 1 : 0;
        for (int i = n-2; i >= 0; i--) {
            cZerosRight[i] = S.charAt(i) == '0' ? cZerosRight[i+1]+1 : cZerosRight[i+1];
        }
        // corner cases: flip until all '0's or all '1's
        for (int i = 0; i < n; i++) {
            cOnesLeft = S.charAt(i) == '1' ? cOnesLeft+1 : cOnesLeft;
            ans = Math.min(ans, i+1 < n ? cOnesLeft + cZerosRight[i+1] : cOnesLeft);
        }
        return Math.min(ans, cZerosRight[0]);
    }
}