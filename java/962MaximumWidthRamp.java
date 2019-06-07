class Solution {
    public int maxWidthRamp(int[] A) {
        int n = A.length;
        // stack of indices with decreasing elements
        Stack<Integer> s = new Stack<Integer>();
        for (int i = 0; i < n; i++) {
            if (s.isEmpty() || A[s.peek()] > A[i])
                s.push(i);
        }
        int ans = 0;
        for (int i = n-1; i >= 0; i--) {
            while (!s.isEmpty() && A[s.peek()] <= A[i])
                ans = Math.max (ans, i - s.pop());
        }
        return ans;
    }
}