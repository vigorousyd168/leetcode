class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int[] minOfRight = new int[n];
        minOfRight[n-1] = arr[n-1];
        // left or right array is inclusive
        for (int i = n-2; i >= 0; i--) {
            minOfRight[i] = Math.min(minOfRight[i+1], arr[i]);
        }
        int maxOfLeft = -1, result = 1; // last chunk is [?..n-1]
        for (int i = 0; i < n-1; i++) {
            maxOfLeft = Math.max(maxOfLeft, arr[i]);
            if (maxOfLeft <= minOfRight[i+1])
                result++; // form a chunk with right bound at i [?..i]
        }
        return result;
    }
}