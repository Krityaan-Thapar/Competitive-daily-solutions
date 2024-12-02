import java.util.ArrayList;

public class Solution {
    static ArrayList<Integer> graph[];
    static int[][] capacity;
    static int[] r, c;
    static int[] visited;
    static int[] parent;

    static boolean getAugumentedpath(int s, int t) {
        visited[s] = 1;
        for (int i = 0; i < graph[s].size(); i++) {
            int adj = graph[s].get(i);

            if (visited[adj] == 0 && capacity[s][adj] > 0) {
                parent[adj] = s;
                if (adj == t) {
                    return true;
                }

                if (getAugumentedpath(adj, t)) {
                    return true;
                }
                parent[adj] = -1;
            }
        }
        return false;
    }

    static int updateAugumentedPath(int n, int m) {
        int minCap = 100000000;
        int node = n + m + 1;

        while (parent[node] != -1) {
            int temp = parent[node];
            minCap = Math.min(minCap, capacity[temp][node]);
            node = temp;
        }

        node = n + m + 1;
        while (parent[node] != -1) {
            int temp = parent[node];
            capacity[temp][node] -= minCap;
            capacity[node][temp] += minCap;
            node = temp;
        }

        return minCap;
    }

    static int maxFlow(int s, int t, int n, int m) {
        int ans = 0;
        int f = 0;
        while (f == 0) {
            for (int i = 0; i < 1003; i++) {
                visited[i] = 0;
                parent[i] = -1;
            }
            if (getAugumentedpath(s, t)) {
                ans += updateAugumentedPath(n, m);
            } else {
                f = 1;
            }
        }
        return ans;
    }
    
    @SuppressWarnings({ "unchecked", "rawtypes" })
    public static int[] maxTrucks(int n, int m, int p, int d, int[][] permits, int[] cap, int[][] reduction) {
        graph = new ArrayList[1002];
        for (int i = 0; i < 1002; i++) {
            graph[i] = new ArrayList();
        }

        capacity = new int[1003][1003];
        r = new int[1003];
        c = new int[1003];
        visited = new int[1004];
        parent = new int[1004];

        for (int i = 1; i <= n; i++) {
            graph[0].add(i);
            graph[i].add(0);
            capacity[0][i] = 1;
        }

        for (int i = 1; i <= p; i++) {
            int u, v;
            u = permits[i - 1][0];
            v = permits[i - 1][1];
            graph[u].add(v + n);
            graph[v + n].add(u);
            capacity[u][v + n] = 1;

        }

        for (int i = n + 1; i <= n + m; i++) {
            graph[i].add(n + m + 1);
            graph[n + m + 1].add(i);
            capacity[i][n + m + 1] = cap[i - n - 1];
        }

        for (int i = 1; i <= d; i++) {
            r[i] = reduction[i - 1][0];
            c[i] = reduction[i - 1][1];
            capacity[n + r[i]][n + m + 1] -= c[i];
        }

        int initialMaxFlow = maxFlow(0, n + m + 1, n, m);
        int[] ans = new int[d];

        while (d > 0) {
            capacity[n + r[d]][n + m + 1] += c[d];
            initialMaxFlow += maxFlow(0, n + m + 1, n, m);
            ans[--d] = initialMaxFlow;
        }
        return ans;
    }
}