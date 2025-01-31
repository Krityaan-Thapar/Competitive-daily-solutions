import java.util.*;

public class Solution {
    public static String reverseVowels(String s){
        HashSet<Character> vowels = new HashSet<Character>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int l = 0, r = s.length() - 1;
        char[] input = s.toCharArray();
        while (l < r) {
            while (l < r && !vowels.contains(input[l])) {
                l++;
            }

            while (l < r && !vowels.contains(input[r])) {
                r--;
            }

            if (l < r) {
                char tmp = input[l];
                input[l] = input[r];
                input[r] = tmp;
                l++;
                r--;
            }
        }
        return new String(input);
    }
}
