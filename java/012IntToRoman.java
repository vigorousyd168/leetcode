import java.util.Hashtable;

public class Solution {
    public String intToRoman(int num) {
        initTable();
        return int2Rom(num, 1000);
    }
    
    private static Hashtable<Integer, String> sTable = new Hashtable<Integer, String>();
    
    private static void initTable ()
    {
        sTable.put(1, "I");
        sTable.put(5, "V");
        sTable.put(10, "X");
        sTable.put(50, "L");
        sTable.put(100, "C");
        sTable.put(500, "D");
        sTable.put(1000, "M");
        sTable.put(5000, "");
        sTable.put(10000, "");
    }
    
    private String repeatStr(String str, int k) {
        String ans = "";
        for (int i = 0; i < k; i++){
            ans += str;
        }
        return ans;
    }
    
    private String int2Rom(int n, int u){
        String ans = "";
        if (u < 1)
            return ans;
        double a = (double)n / (5*u);
        if (a < 0.8){
            int k = n / u;
            return repeatStr(sTable.get(u), k) + int2Rom(n-k*u, u/10);
        }
        else if (a < 1){
            return sTable.get(u) + sTable.get(5*u) + int2Rom(n-4*u, u);
        }
        else if (a < 1.8){
            return sTable.get(5*u) + int2Rom(n-5*u, u);
        }
        else{ // a < 2
            return sTable.get(u) + sTable.get(10*u) + int2Rom(n-9*u, u);
        }
    }
}