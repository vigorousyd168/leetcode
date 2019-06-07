class Solution {
    public List<String> commonChars(String[] A) {
        int[] count = new int[26];
        List<String> ans = new ArrayList<String>();
        for (char c : A[0].toCharArray()) {
            count[c - 'a']++;
        }
        
        for (int j = 0; j < A.length; j++) {
            for (int i = 0 ; i < 26; i++) {
                if (count[i] != 0) {
                    int cnt = 0;
                    for (char c : A[j].toCharArray()) {
                        if (c - 'a' == i) cnt++;
                    }
                    if (cnt < count[i])
                        count[i] = cnt;
                }
            }
        }
        for (int i = 0 ; i < 26; i++) {
            for (int k = 0; k < count[i]; k++) {
                ans.add(Character.toString((char)(i+'a')));
            }
        }
        return ans;
    }
}