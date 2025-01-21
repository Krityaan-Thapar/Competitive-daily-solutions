public class Solution {
    public static int toggleKBits(int n, int k) {
        for (int i = 0; i < k; i++) {
            int raiser = 1 << i;
            n = n ^ raiser;
        }
        return n;
    }
}