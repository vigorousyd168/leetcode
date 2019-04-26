class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        // ends with >= 2 0's -> true
        // how many 1's before the ending 0:
        // odd -> false
        // even -> true
        int countOnes = 0;
        for (int i = bits.length-2; i >= 0 ; i--) {
            if (bits[i] == 0) break;
            else countOnes++;
        }
        if (countOnes % 2 == 0) return true;
        else return false;
    }
}