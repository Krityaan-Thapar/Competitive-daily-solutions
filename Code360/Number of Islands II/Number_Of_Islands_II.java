import java.util.ArrayList;
import java.util.List;

class DSU {
    int[] e;
    DSU(int N) {
        e = new int[N];
        for (int i = 0; i < N; i++) {
            e[i] = -1;
        }
    }

    int get(int x) {
        if (e[x] < 0)
            return x;
        else {
            e[x] = get(e[x]);
            return e[x];
        }
    }

    boolean same_set(int a, int b) {
        return get(a) == get(b);
    }

    int size(int x) {
        return -e[get(x)];
    }

    boolean merge(int x, int y) {
        x = get(x);
        y = get(y);
        if (x == y)
            return false;
        if (e[x] > e[y])
            swap(x, y);
        e[x] += e[y];
        e[y] = x;
        return true;
    }

    void swap(int x, int y) {
        int temp = e[x];
        e[x] = e[y];
        e[y] = temp;
    }
}

class Number_Of_Islands_II {
    public static int[] numberOfIslandII(int n, int m, int[][] queries, int q) {
        DSU d = new DSU(n * m);

        int[] dx = { -1, 0, 1, 0 };
        int[] dy = { 0, -1, 0, 1 };

        int[][] grid = new int[n][m];
        List<Integer> ans = new ArrayList<>();
        int count = 0;

        for (int[] query : queries) {
            int x = query[0], y = query[1];

            grid[x][y] = 1;
            count++;

            for (int i = 0; i < 4; i++) {
                int a = x + dx[i];
                int b = y + dy[i];

                if (a >= 0 && a < n && b >= 0 && b < m && grid[a][b] == 1) {
                    if (!d.same_set(x * m + y, a * m + b)) {
                        count--;
                        d.merge(x * m + y, a * m + b);
                    }
                }
            }

            ans.add(count);
        }
        
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }

        return result;
    }
}
