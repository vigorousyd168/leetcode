class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        int[] result = new int[A.length];
        int[] sortedA = A.clone();
        int[] sortedB = B.clone();
        Arrays.sort(sortedA);
        Arrays.sort(sortedB);
        Map<Integer, Deque<Integer>> used = new HashMap<Integer, Deque<Integer>>();
        Deque<Integer> unused = new LinkedList<Integer>();
        for (int b : B) {
            used.put(b, new LinkedList<Integer>());
        }
        int j = 0;
        for (int a : sortedA) {
            if (a > sortedB[j])
                used.get(sortedB[j++]).add(a);
            else
                unused.add(a);
        }
        for (int i = 0; i < B.length; i++) {
            if (used.get(B[i]).size() > 0)
                result[i] = used.get(B[i]).removeFirst();
            else
                result[i] = unused.removeFirst();
        }
        return result;
    }
}