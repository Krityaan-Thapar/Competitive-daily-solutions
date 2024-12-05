public class Solution {
    
    static boolean valid(int x, int y, int n) {
        return x >= 0 && y >= 0 && x < n && y < n;
    }

    static int[] game(int n, int[] a, int[] o, int[] x, int[] z) {
        a[0]--;
        a[1]--;
        o[0]--;
        o[1]--;
        x[0]--;
        x[1]--;
        z[0]--;
        z[1]--;

        int d[][] = new int[2][2];
        d[0][0] = 1;
        d[0][1] = 0;
        d[1][0] = 0;
        d[1][1] = 1;

        int zt[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                zt[i][j] = n;
            }
        }

        for (int time = 0; time < n; time++) {
            zt[z[0]][z[1]] = time;

            int i = time % 2;
            int dx = z[0] + d[i][0];
            int dy = z[1] + d[i][1];
            if (dx >= n || dx < 0) {
                d[0][0] *= -1;
            }
            if (dy >= n || dy < 0) {
                d[1][1] *= -1;
            }
            z[0] = z[0] + d[i][0];
            z[1] = z[1] + d[i][1];
        }

        int t[][] = new int[n][n];
        int dir[] = new int[2];

        int total = n - 1;
        if (a[0] == 0) {
            dir = new int[] { 1, 0 };
            total = n - a[0] - 1;
        } else if (a[0] == n - 1) {
            dir = new int[] { -1, 0 };
            total = a[0];
        } else if (a[1] == 0) {
            dir = new int[] { 0, 1 };
            total = n - a[1] - 1;
        } else {
            dir = new int[] { 0, -1 };
            total = a[1];
        }

        int[] dx = { 1, 0, -1, 0, -1, -1, 1, 1 };
        int[] dy = { 0, 1, 0, -1, -1, 1, -1, 1 };
        for (int i = 0; i < total; i++) {
            if (i == x[0]) {
                if ((a[0] + a[1]) % 2 == (x[0] + x[1]) % 2) {
                    return new int[] { a[0] + 1, a[1] + 1 };
                }
            }

            if (i % 4 == 3) {
                t[x[0]][x[1]] -= 3;
            } else {
                t[x[0]][x[1]]++;
            }

            if (i % 4 == 1) {
                for (int k = 0; k < 8; k++) {
                    int ii = x[0] + dx[k];
                    int j = x[1] + dy[k];
                    if (!valid(ii, j, n))
                        continue;
                    t[ii][j]++;
                }
            }

            if (t[a[0]][a[1]] != 0 || zt[a[0]][a[1]] <= i) {
                return new int[] { a[0] + 1, a[1] + 1 };
            }

            if (i % 4 == 1) {
                for (int k = 0; k < 8; k++) {
                    int ii = x[0] + dx[k];
                    int j = x[1] + dy[k];
                    if (!valid(ii, j, n))
                        continue;
                    t[ii][j]--;
                }
            }
            a[0] += dir[0];
            a[1] += dir[1];
        }
        return new int[] { -1, -1 };
    }
}