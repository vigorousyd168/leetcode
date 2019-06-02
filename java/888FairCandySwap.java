class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int sumA = 0, sumB = 0;
        Set<Integer> set = new HashSet<Integer> ();
        for (int i = 0; i < A.length; i++) {
            set.add(A[i]);
            sumA += A[i];
        }
        for (int j = 0; j < B.length; j++) {
            sumB += B[j];
        }
        for (int j = 0; j < B.length; j++) {
            if (set.contains(B[j] - (sumB-sumA)/2))
                return new int[] {B[j] - (sumB-sumA)/2, B[j]};
        }
        return null;
    }
}