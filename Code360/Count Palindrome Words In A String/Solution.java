public class Solution {
    public static int countNumberOfPalindromeWords(String s) {
        if (s == null || s == "" || s.length() == 0) {
            return 0;
        }

        String[] arr = s.split("[ \\t]+");
        int ans = 0;

        for (String word : arr) {
            word = word.toLowerCase();
            int l = 0, r = word.length() - 1;
            boolean pal_flag = true;
            
            while (l <= r) {
                if (word.charAt(l) != word.charAt(r)) {
                    pal_flag = false;
                    break;
                }
                l++;
                r--;
            }

            if (pal_flag) {
                ans++;
            }
        }
        return ans;
    }
}