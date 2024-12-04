public class Solution {
    public static String maximumDifference(int n, int[] arr) {
        int max = -1;
        int min = 1000000001;
        for (int i : arr) {
            if (i < min) {
                min = i;
            }

            if (i > max) {
                max = i;
            }
        }

        int diff = max - min;
        if (diff % 2 == 0) {
            return "EVEN";
        }
        return "ODD";
    }
}