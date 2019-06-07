class Solution {
    public List<Integer> pancakeSort(int[] A) {
        // fix right to left
        Integer n = A.length;
        List<Integer> ans = new ArrayList<Integer>();
        Integer[] sortedIdx = new Integer[n];
        for (int i = 0; i < n; i++)
            sortedIdx[i] = i;
        // sort (decreasing)
        Arrays.sort(sortedIdx, (i,j) -> (A[j] - A[i]));
        for (Integer idx : sortedIdx)
        {
            // reverse  first (idx+1) numbers so that A[idx] will be at A[0]
            for (Integer f : ans)
            {
                // previous flips may have changed the position of idx
                if (idx < f)
                    idx = f-1-idx;
            }
            ans.add(idx+1);
            ans.add(n--);
        }
        return ans;
    }
}