class Solution {
    public int maxDistToClosest(int[] seats) {
        int result = 1, zeros = 0;
        boolean leftZero = seats[0] == 0;
        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 0) {
                zeros++;
                if (i == seats.length-1) {
                    result = Math.max(result, zeros);
                }
            }
            else {
                if (leftZero) {
                    result = zeros;
                    leftZero = false;
                }
                result = Math.max(result, (zeros+1)/2);
                zeros = 0;
            }
        }
        return result;
    }
}