class Solution {
    public int sumSubarrayMins(int[] A) {
        int mod = 1000000007;
        int n = A.length;
        Stack<Integer> s = new Stack<Integer>();
        // construct left bounds array
        // left[i] is the left (not-inclusive) bound index for A[i] where the min uses A[i]
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            while (!s.isEmpty() && A[s.peek()] >= A[i]) s.pop(); // >=
            left[i] = s.isEmpty()? -1 : s.peek();
            s.push(i);
        }
        // construct right bounds array
        int[] right = new int[n];
        s = new Stack();
        for (int i = n-1; i >=0; i--) {
            while (!s.isEmpty() && A[s.peek()] > A[i]) s.pop(); // >
            right[i] = s.isEmpty()? n : s.peek();
            s.push(i);
        }
        long sum = 0, prod;
        for (int i = 0; i < n; i++) {
            prod = A[i] * (i-left[i]) * (right[i]-i) % mod;
            sum += prod % mod;
            sum %= mod;
        }
        return (int) sum;
    }
}