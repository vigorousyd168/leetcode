class Solution {
    public int leastInterval(char[] tasks, int n) {
        // need proof:
        // A_n_A_n_A______ if count(A) = c,
        // num of slots after last A is (num of tasks that appear c times - 1).
        int len = tasks.length;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        // stores <char, count>
        int count, max = 0;
        for (int i = 0; i < len; i++) {
            count = map.getOrDefault(tasks[i], 0) + 1;
            map.put(tasks[i], count);
            if (count > max) max = count;
        }
        int countLongestTasks = 0;
        for (Map.Entry<Character,Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) countLongestTasks++;
        }
        return Math.max(len, max*(1+n)-n+countLongestTasks-1);
    }
}

class Solution {
    public int leastInterval(char[] tasks, int n) {
        // need proof:
        // A_n_A_n_A______ if count(A) = c,
        // num of slots after last A is (num of tasks that appear c times - 1).
        int len = tasks.length;
        int[] map = new int[26];
        int max = 0;
        for (char c : tasks) {
            map[c - 'A']++;
            if (map[c - 'A'] > max) max = map[c - 'A'];
        }
        int countLongestTasks = 0;
        for (int i = 0; i < 26; i++) {
            if (map[i] == max) countLongestTasks++;
        }
        return Math.max(len, max*(1+n)-n+countLongestTasks-1);
    }
}