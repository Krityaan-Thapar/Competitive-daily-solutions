public class Solution {
    public static void printPattern(int n) {
        for (int row = 1; row <= n; row++) {
            int spaces = 0;
            while (spaces < n - row) {
                System.out.print(" ");
                spaces += 1;
            }

            for (int col = 1; col <= 2 * row - 1; col++) {
                System.out.print("*");
            }
            System.out.println(" ");
        }
    }
}