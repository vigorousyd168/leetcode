public class Solution {
    public int reverse(int x) {
        int result = 0;
        int d, newResult;
        // handles positive and negative numbers
        while (x != 0) {
            // get last digit
            d = x % 10;
            // use the digit in the result
            newResult = result*10 + d;
            if ((newResult - d) / 10 != result) {
                return 0; // overflow
            }
            else {
                x = x / 10;
                result = newResult;
            }
        }
        return result;
    }
}