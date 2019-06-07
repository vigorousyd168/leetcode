class Solution {
    public int maxScoreSightseeingPair(int[] A) {
        // every time we move forward, the score of a visited node decrements by 1
        int result = 0, preMax = 0;
        for (int i = 0; i < A.length; i++)
        {
            result = Math.max(result, A[i] + preMax);
            preMax = Math.max(preMax, A[i]) - 1;
        }
        return result;
    }
}