class Solution {
    public int maxTurbulenceSize(int[] A) {
        int n = A.length;
        // # of turbulent array ending at i and last sign is +
        int lastUp = 1;
        // # of turbulent array ending at i and last sign is -
        int lastDown = 1;
        int ans = 1, temp;
        for (int i = 1; i < n; i++) {
            temp = lastUp;
            lastUp = A[i] > A[i-1] ? lastDown + 1 : 1;
            lastDown = A[i] < A[i-1] ? temp + 1 : 1;
            if (lastUp > ans) ans = lastUp;
            if (lastDown > ans) ans = lastDown;
        }
        return ans;
    }
}