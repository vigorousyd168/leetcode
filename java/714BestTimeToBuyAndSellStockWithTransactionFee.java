class Solution {
    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 0; i < prices.length; i++) {
            cash = Math.max(cash, hold + prices[i] - fee);
            // if cash is prev cash, this change won't affect the line below
            // otherwise cash is hold+prices[i]-fee
            // so cash-prices[i] = hold-fee < hold, left is used in the Math.max op below
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }
}