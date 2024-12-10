import java.util.*;

public class Solution {
    public static boolean check(int mid, int k, ArrayList<Integer> element) {
        int current = 0, parts = 1;

        for (int i = 0; i < element.size(); i++) {
            if (element.get(i) > mid) {
                return false;
            } else if (current + element.get(i) > mid) {
                current = element.get(i);
                parts++;
            } else {
                current += element.get(i);
            }
        }

        if (parts <= k) {
            return true;
        }
        return false;
    }

    public static int splitArray(ArrayList<Integer> array, int k) {
        int n = array.size();
        int minimum = Collections.max(array), maximum = 0;

        for (int i = 0; i < n; i++) {
            maximum += array.get(i);
        }
        while (minimum <= maximum) {
            int mid = (minimum + maximum) / 2;
            if (check(mid, k, array) == true) {
                maximum = mid - 1;
            } else {
                minimum = mid + 1;
            }
        }
        return minimum;
    }
}