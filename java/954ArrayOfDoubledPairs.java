class Solution {
    public boolean canReorderDoubled(int[] A) {
        // difficult part is negative value... so we sort by abs
        int n = A.length;
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        for (int a : A) count.put(a, count.getOrDefault(a, 0) + 1);
        Integer[] B = new Integer[n];
        for (int i = 0; i < n; i++) B[i] = A[i];
        Arrays.sort(B, Comparator.comparingInt(Math::abs)); // sort by abs, so 2x always appears after x
        for (int b : B) {
            if (count.get(b) == 0) continue;
            if (count.getOrDefault(2*b, 0) <= 0) return false;
            count.put(b, count.get(b)-1);
            count.put(2*b, count.get(2*b)-1);
        }
        return true;
    }
}