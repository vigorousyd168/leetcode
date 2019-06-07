class Solution {
    public List<Boolean> prefixesDivBy5(int[] A) {
        List<Boolean> res = new ArrayList<Boolean>();
        int m = 0;
        for (int i = 0; i < A.length; i++)
        {
            m = (2 * m + A[i]) % 5;
            res.add(m % 5 == 0 ? true : false);
        }
        return res;
    }
}