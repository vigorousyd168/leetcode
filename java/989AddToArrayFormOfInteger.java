class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> ans = new ArrayList<Integer>();
        int n = A.length, carry = 0, d, sum;
        int i = 0;
        while (i < n || K > 0 || carry > 0) {
            // right to left
            sum = K%10 + carry;
            if (n-1-i >= 0) sum += A[n-1-i];
            d = sum % 10;
            carry = sum / 10;
            K /= 10;
            ans.add(d);
            i++;
        }
        Collections.reverse(ans);
        return ans;
    }
}