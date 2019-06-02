class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int result = 0, max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, arr[i]);
            if (max == i) result++;
        }
        return result;
    }
}