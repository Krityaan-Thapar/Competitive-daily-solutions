import java.util.Stack;
import java.util.ArrayList;
import java.util.Arrays;

class help {
    int x;
}

public class Biconnected_Components {
    static int time = 0;
    static void dfs(int u, int[] disc, int[] low, Stack<pair<Integer, Integer>> st, int[] parent, ArrayList<ArrayList<Integer>> adj, help count) {
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                children++;
                parent[v] = u;

                st.push(new pair<Integer, Integer>(u, v));
                dfs(v, disc, low, st, parent, adj, count);
                low[u] = Math.min(low[u], low[v]);

                if ((disc[u] == 1 && children > 1) || (disc[u] > 1 && low[v] >= disc[u])) {
                    while (st.peek().first != u || st.peek().second != v) {
                        st.pop();
                    }
                    st.pop();
                    count.x++;
                }
            }

            else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
                if (disc[v] < disc[u]) {
                    st.push(new pair<Integer, Integer>(u, v));
                }

            }
        }

    }

    public static int biconnectedComponents(int n, int m, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(edges[i][1]);
            adj.get(edges[i][1]).add(edges[i][0]);
        }
        help count = new help();
        int[] disc = new int[n + 1];
        int[] low = new int[n + 1];
        int[] parent = new int[n + 1];
        Arrays.fill(disc, -1);
        Arrays.fill(low, -1);
        Arrays.fill(parent, -1);

        Stack<pair<Integer, Integer>> st = new Stack<>();
        for (int i = 1; i <= n; i++) {
            if (disc[i] == -1) {
                dfs(i, disc, low, st, parent, adj, count);
            }
            if (st.size() > 0) {
                count.x++;
            }
            while (st.size() > 0) {
                st.pop();
            }
        }

        return count.x;
    }
}

class pair<X, Y> {
    X first;
    Y second;

    pair(X x, Y y) {
        this.first = x;
        this.second = y;
    }
}
