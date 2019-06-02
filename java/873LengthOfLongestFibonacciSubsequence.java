class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int n = A.length;
        int result = 0;
        Map<Integer, Integer> idx = new HashMap<Integer, Integer> ();
        // length of longest fib like subseq ending with A[i], A[j] (encoded into i*n+j)
        Map<Integer, Integer> longest = new HashMap<Integer, Integer> ();
        
        for (int i = 0; i < n; i++) {
            idx.put(A[i], i);
        }
        for (int k = 0; k < n; k++) {
            for (int j = 0; j < k; j++) {
                if (idx.containsKey(A[k]-A[j])) {
                    int i = idx.get(A[k]-A[j]);
                    if (i < j) {
                        int len = longest.getOrDefault(i*n+j, 2) + 1; // [i,j]
                        longest.put(j*n+k, len); // [j,k]
                        result = Math.max(result, len);
                    }
                }
            }
        }
        return result;
    }
}