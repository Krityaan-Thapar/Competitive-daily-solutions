import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    private static ArrayList<Integer> topologicalSort(HashMap<Integer, ArrayList<Integer>> graph) {
        HashMap<Integer, Integer> inDegree = new HashMap<>();

        for (HashMap.Entry<Integer, ArrayList<Integer>> entry : graph.entrySet()) {
            int node = entry.getKey();
            inDegree.put(node, 0);
        }
        for (HashMap.Entry<Integer, ArrayList<Integer>> entry : graph.entrySet()) {
            int node = entry.getKey();

            for (int i = 0; i < graph.get(node).size(); i++) {
                int child = graph.get(node).get(i);
                if (inDegree.containsKey(child)) {
                    inDegree.put(child, inDegree.get(child) + 1);
                } else {
                    inDegree.put(child, 1);
                }

            }
        }

        Queue<Integer> q = new LinkedList<>();
        for (HashMap.Entry<Integer, Integer> entry : inDegree.entrySet()) {
            int node = entry.getKey();
            if (inDegree.get(node) == 0) {
                q.add(node);
            }
        }

        ArrayList<Integer> nodes = new ArrayList<>();
        while (!q.isEmpty()) {
            int currNode = q.peek();
            q.poll();
            nodes.add(currNode);
            for (int i = 0; graph.containsKey(currNode) && i < graph.get(currNode).size(); i++) {
                int child = graph.get(currNode).get(i);
                inDegree.put(child, inDegree.get(child) - 1);
                if (inDegree.get(child) == 0)
                    q.add(child);
            }
        }
        return nodes;
    }

    public static int[] makeArray(int n, int[][] subsequences) {
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for (int i = 0; i < subsequences.length; i++) {
            int subseq[] = subsequences[i];

            for (int j = 1; j < subseq.length; j++) {
                if (graph.containsKey(subseq[j - 1])) {
                    ArrayList<Integer> list = graph.get(subseq[j - 1]);
                    list.add(subseq[j]);
                } else {
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(subseq[j]);
                    graph.put(subseq[j - 1], list);
                }

            }
        }
        ArrayList<Integer> ans = topologicalSort(graph);
        int ansArr[] = new int[ans.size()];

        for (int i = 0; i < ans.size(); i++) {
            ansArr[i] = ans.get(i);
        }
        return ansArr;
    }
}