/*
    
        Time Complexity : O(W * N)
            Space Complexity : O(W)

                where 'W' is number of valid words and 'N' is length of sequence of digits.

                */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;

public class Solution {
    public static ArrayList<String> phoneCode(ArrayList<String> Words, String Sequence, int W) {
        ArrayList<String> Alphabets = new ArrayList<String>(
                Arrays.asList("abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"));
        HashMap<Character, Integer> mp = new HashMap<Character, Integer>();

        for (int i = 0; i < Alphabets.size(); i++) {
            for (int j = 0; j < Alphabets.get(i).length(); j++) {
                mp.put(Alphabets.get(i).charAt(j), i + 2);
            }
        }

        ArrayList<String> result = new ArrayList<String>();
        int number;
        char ch;

        for (int i = 0; i < W; i++) {
            number = 0;
            for (int j = 0; j < Words.get(i).length(); j++) {
                ch = Words.get(i).charAt(j);
                number = number * 10 + mp.get(ch);
            }

            int n = Integer.parseInt(Sequence);
            if (number == (n)) {
                result.add(Words.get(i));
            }
        }
        return result;
    }
}