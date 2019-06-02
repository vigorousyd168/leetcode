class Solution {
    public List<List<Integer>> largeGroupPositions(String S) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (S.length() == 0) return result;
        int currLen = 1, start = 0;
        char prev = S.charAt(0), curr;
        for (int i = 1; i < S.length(); i++) {
            curr = S.charAt(i);
            if (curr == prev) {
                currLen++;
                if (i == S.length()-1) { // special case: last k letters are the same
                    if (currLen >= 3)
                        result.add(Arrays.asList(start, i));
                }
            }
            else {
                if (currLen >= 3)
                    result.add(Arrays.asList(start, i-1));
                currLen = 1;
                start = i;
            }
            prev = curr;
        }
        return result;
    }
}