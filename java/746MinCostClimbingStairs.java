class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n == 0) return 0;
        if (n == 1) return cost[0];
        if (n == 2) return cost[1];
        int[] minCost = new int[n]; // min cost to reach the i-th step (but cost[i] not yet counted)
        minCost[0] = 0;
        minCost[1] = 0;
        for (int i = 2; i < n; i++) {
            minCost[i] = Math.min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2]);
        }
        return Math.min(minCost[n-2] + cost[n-2], minCost[n-1] + cost[n-1]);
    }
}