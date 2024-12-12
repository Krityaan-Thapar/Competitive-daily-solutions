import java.util.*;

public class Solution {
    public static Boolean canChange(String k, String s) {
        if (k.equals(s)) {
            return true;
        }

        if (k.length() != s.length()) {
            return false;
        }

        int []check = new int[26];
        for (int i = 0; i < s.length(); i++) {
            check[s.charAt(i) - 97]++;
        }

        int c = 0;
        for (int i = 0; i < 26; i++) {
            if (check[i] >= 1) {
                c++;
            }
        }
        
        if (c == 26) {
            return false;
        } 
        
        HashMap<Character, Character> m = new HashMap<>();
        for (int i = 0; i < k.length(); i++) {
            if (m.containsKey(k.charAt(i)) == false) {
                m.put(k.charAt(i), s.charAt(i));
            } else if (!m.get(k.charAt(i)).equals(s.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}