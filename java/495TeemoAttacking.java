class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int n = timeSeries.length, result = 0, start = 0, end = 0;
        for (int i = 0; i < n; i++) {
            if (timeSeries[i] < end){
                result += timeSeries[i] - start;
            }
            else
                result += duration;
            start = timeSeries[i];
            end = start + duration;
        }
        return result;
    }
}