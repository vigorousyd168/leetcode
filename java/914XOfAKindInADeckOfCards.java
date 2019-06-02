class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        for (int card : deck) {
            count.put(card, count.getOrDefault(card, 0) + 1);
        }
        int minCount = deck.length;
        for (int cnt : count.values()) {
            if (cnt < minCount) minCount = cnt;
        }
        if (minCount < 2) return false;
        // check if all counts have a common divider (not necessarily gcd) >= 2
        for (int i = 2; i <= minCount; i++) {
            boolean found = true;
            for (int cnt : count.values()) {
                if (cnt % i != 0) {
                    found = false;
                    break;
                }
            }
            if (found) return true;
        }
        return false;
    }
}