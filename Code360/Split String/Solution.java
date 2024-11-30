import java.util.*;
 
public class Solution {
    public static Boolean splitString(String str) {
        HashSet<Character> vowels = new HashSet<Character>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');

        int l = str.length();
        int c = 0;
        for (int i = 0; i < l; i++) {
            if (vowels.contains(str.charAt(i))) {
                if (i >= l / 2) {
                    c -= 1;
                } else {
                    c += 1;
                }
            }
        }

        return c == 0;
    }

}