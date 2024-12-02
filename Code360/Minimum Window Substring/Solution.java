import java.util.HashMap;

public class Solution {
    public static String minSubString(String a, String b) {
        if (a.length() < b.length()) {
            return "-1";
        }

        int b_s = b.length();
        HashMap<Character, Integer> need = new HashMap<Character, Integer>();
        for (int i = 0; i < b.length(); i++) {
            char ch = b.charAt(i);
            need.put(ch, need.getOrDefault(ch, 0) + 1);
        }
        int[] ans = new int[2];
        ans[0] = 0;
        ans[1] = a.length() + 1;

        int l = 0;
        for (int r = 0; r < a.length(); r++) {
            char curr = a.charAt(r);
            if (need.getOrDefault(curr, 0) > 0) {
                b_s--;
            }
            need.put(curr, need.getOrDefault(curr, 0) - 1);

            if (b_s == 0) {
                while (true) {
                    char tmp = a.charAt(l);
                    if (need.get(tmp) == 0) {
                        break;
                    }
                    need.put(tmp, need.get(tmp) + 1);
                    l++;
                }
                
                if (r - l < ans[1] - ans[0]) {
                    ans[0] = l;
                    ans[1] = r;
                }
                need.put(a.charAt(l), need.get(a.charAt(l)) + 1);
                b_s++;
                l++;
            }
        }
        if (ans[1] > a.length()) {
            return "-1";
        }
        return a.substring(ans[0], ans[1] + 1);
    }
}