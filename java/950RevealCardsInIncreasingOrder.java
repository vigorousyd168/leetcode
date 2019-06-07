class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int[] sortedDeck = deck.clone();
        int n = deck.length;
        Arrays.sort(sortedDeck);
        LinkedList<Integer> list = new LinkedList<Integer>();
        list.add(sortedDeck[n-1]);
        for (int i = n-2; i >= 0; i--) {
            list.addFirst(list.removeLast());
            list.addFirst(sortedDeck[i]);
        }
        int[] ans = new int[n];
        int i = 0;
        while (i < n) ans[i++] = list.poll();
        return ans;
    }
}