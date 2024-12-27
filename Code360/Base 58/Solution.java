import java.util.* ;

public class Solution {
    public static String encodeBase58(int n){
        if (n == 0) {
            return "1";
        }
        
        String m = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
        ArrayList<String> store = new ArrayList<>();
        
        while (n > 0) {
            int t = n % 58;
            n = n / 58;
            store.add(m.substring(t, t + 1));
        }

        String ans = "";
        for (int i = store.size() - 1; i >= 0; i--) {
            ans = ans + store.get(i);
        }
        return ans;
    }
}