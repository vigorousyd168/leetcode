class Solution {
    public int maxSubarraySumCircular(int[] A) {
        // two cases: 1) C does not cross the border
        // 2) C does cross the border, think in the opposite way
        // the problem is equivalent to finding min-sum B where B = A / C
        int sumA = 0;
        for (int a : A) sumA += a;
        // case 1
        int maxSum = -30000-A[0], globalMaxSum = A[0];
        for (int i = 0; i < A.length; i++) {
            // DP: maxSum is a sum of array ending at i
            maxSum = Math.max(maxSum + A[i], A[i]);
            globalMaxSum = Math.max(globalMaxSum, maxSum);
        }
        // case 2
        int minSum = 30000-A[0], globalMinSum = A[0];
        for (int i = 1; i < A.length; i++) {
            minSum = Math.min(minSum + A[i], A[i]);
            globalMinSum = Math.min(globalMinSum, minSum);
            System.out.println(globalMinSum);
        }
        return Math.max(globalMaxSum, sumA - globalMinSum);
    }
}