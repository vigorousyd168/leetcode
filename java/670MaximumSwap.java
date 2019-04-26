class Solution {
    public int maximumSwap(int num) {
        // process from right to left
        // swap {first occurance of max digit}
        // with {last occurance of non-max digit}
        int n = String.valueOf(num).length();
        int rest = num;
        int digit, maxDigit = 0, firstMaxPos = 0, smallerDigit = 0, lastSmallerPos = 0, swapDigit = 0, swapPos = 0;
        // right to left
        for (int i = 0; i < n; i++) {
            digit = rest % 10;
            rest /= 10;
            if (digit > maxDigit) {
                maxDigit = digit;
                firstMaxPos = i;
            }
            else if (digit < maxDigit) {
                smallerDigit = digit;
                lastSmallerPos = i;
                swapDigit = maxDigit;
                swapPos = firstMaxPos;
            }
        }
        if (lastSmallerPos == 0)
            return num;
        else {
            return num + (int)((swapDigit-smallerDigit)*Math.pow(10,lastSmallerPos)) - (int)((swapDigit-smallerDigit)*Math.pow(10,swapPos));
        }
    }
}