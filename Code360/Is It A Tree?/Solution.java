import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution {

    public static boolean isCyclicConntected(ArrayList<ArrayList<Integer>> adj, int s, int V, boolean visited[]) {
        int parent[] = new int[V];
        for (int i = 0; i < V; i++) {
            parent[i] = -1;
        }

        Queue<Integer> q = new LinkedList<>();
        visited[s] = true;
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int i = 0; i < adj.get(u).size(); i++) {
                int v = adj.get(u).get(i);
                if (!visited[v]) {
                    visited[v] = true;
                    q.add(v);
                    parent[v] = u;
                } else if (parent[u] != v)
                    return true;
            }
        }
        return false;
    }

    public static boolean isTree(ArrayList<ArrayList<Integer>> adj, int V) {
        boolean[] visited = new boolean[V];
        if (isCyclicConntected(adj, 0, V, visited))
            return false;
        
        for (int i = 0; i < V; i++) {
            if (visited[i] == false) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int V = s.nextInt();
        int E = s.nextInt();

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            adj.add(list);
        }
        for (int i = 0; i < E; i++) {
            int x = s.nextInt();
            int y = s.nextInt();
            adj.get(x).add(y);
            adj.get(y).add(x);
        }
        s.close();

        if (isTree(adj, V))
            System.out.println("True");
        else {
            System.out.println("False");
        }
    }
}
