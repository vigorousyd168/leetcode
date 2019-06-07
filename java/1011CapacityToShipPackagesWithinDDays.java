class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int n = weights.length;
        int[] preSum = new int[n+1];
        int sum = 0, max = weights[0];
        for (int i = 0; i < n; i++) {
            sum += weights[i];
            preSum[i+1] = sum;
            if (weights[i] > max) max = weights[i];
        }
        // preSum[i+1] is the sum of weights[0]..weights[i]
        // so sum of weights[i]..weights[j] is preSum[j+1] - preSum[i]
        int low = max, high = preSum[n];
        while (low <= high) {
            if (low == high) return low;
            int mid = (low+high)/2;
            int start = 0, end = 0, days = 0;
            while (start < n) {
                while (end < n && preSum[end+1] - preSum[start] <= mid) end++;
                if (++days > D) {
                    low = mid+1;
                    break;
                }
                start = end;
            }
            if (days <= D) high = mid;
        }
        return max;
    }
}