public class Solution {
    public static void setZeros(int matrix[][]) {
        int m = matrix.length, n = matrix[0].length;
        boolean fc = false, fr = false;
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                fc = true;
                break;
            }
        }

        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == 0) {
                fr = true;
                break;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        
        for (int i = 1; i < m; i++) { 
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (fr) {
            for (int i = 0; i < n; i++) {
                matrix[0][i] = 0;
            }
        }

        if (fc) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}