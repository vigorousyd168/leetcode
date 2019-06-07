class Solution {
    public int numFriendRequests(int[] ages) {
        int n = ages.length;
        int[] count = new int[121]; // 1 <= ages[i] <= 120
        for (int age : ages) count[age] += 1;
        int ans = 0;
        for (int age1 = 1; age1 <= 120; age1++) {
            if (count[age1] > 0) {
                int age2 = (int)Math.floor(age1 * 0.5) + 8;
                while (age2 < age1) {
                    ans += count[age1] * count[age2++];
                }
                if (age2 == age1)
                    ans += count[age1] * (count[age2]-1); // do not count self
            }
        }
        return ans;
    }
}