public class Solution {
    public static boolean isConvexPolygon(int points[][], int n) {
        int positive = 0, negative = 0;

        for (int a = 0; a < n; a++) {
            int b = (a + 1) % n;
            int c = (b + 1) % n;
            int xA = points[a][0], yA = points[a][1];
            int xB = points[b][0], yB = points[b][1];
            int xC = points[c][0], yC = points[c][1];
            int pos = (xA - xB) * (yC - yB) - (yA - yB) * (xC - xB);

            if (pos > 0) {
                positive = 1;
            } else if (pos < 0) {
                negative = 1;
            }

            if (positive > 0 && negative > 0) {
                return false;
            }
        }
        return true;
    }
}