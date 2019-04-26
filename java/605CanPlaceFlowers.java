class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        int consecutiveZeros = 1; // special case: leftmost slot
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                consecutiveZeros++;
                if (consecutiveZeros > 2) {
                    n--;
                    if (n == 0) return true;
                    consecutiveZeros = 1;
                }
            }
            else // 1
                consecutiveZeros = 0;
        }
        if (consecutiveZeros == 2) n--; // special case: rightmost slot
        return n == 0;
    }
}