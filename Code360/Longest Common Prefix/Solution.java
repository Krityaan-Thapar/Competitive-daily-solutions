import java.util.*;

class Node {
    Node[] alpha = new Node[26];
    int cntLetter = 0;
    boolean flag = false;

    Node() {
    }

    boolean contains(char ch) {
        return alpha[ch - 'a'] != null;
    }

    void put(char ch, Node node) {
        alpha[ch - 'a'] = node;
    }

    Node get(char ch) {
        return alpha[ch - 'a'];
    }

    void setCnt() {
        cntLetter++;
    }

    int getCnt() {
        return cntLetter;
    }

    void setEnd() {
        flag = true;
    }

    boolean getEnd() {
        return flag;
    }
}

class Trie {
    Node root;

    Trie() {
        root = new Node();
    }

    void insert(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!node.contains(ch)) {
                node.put(ch, new Node());
            }
            node = node.get(ch);
            node.setCnt();
        }
        node.setEnd();
    }

    int lengthOfPrefix(String word) {
        int ans = 0;
        Node node = root;
        int i = 0;
        for (; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!node.contains(ch)) {
                break;
            }
            node = node.get(ch);
            ans += node.getCnt();

        }
        return ans;
    }
}

public class Solution {
    public static int[] noOfSteps(int N, String[] db, int q, String[] queries) {
        Trie trie = new Trie();
        int[] ans = new int[q];
        Map<String, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < q; i++) {
            if (!map.containsKey(queries[i])) {
                map.put(queries[i], new ArrayList<>());
            }
            map.get(queries[i]).add(i);
        }
        for (int i = 0; i < N; i++) {
            trie.insert(db[i]);
            if (map.containsKey(db[i])) {
                for (int idx : map.get(db[i])) {
                    ans[idx] = (i + 1) + trie.lengthOfPrefix(db[i]);
                }
            }
        }
        for (int i = 0; i < q; i++) {
            if (ans[i] == 0) {
                ans[i] = N + trie.lengthOfPrefix(queries[i]);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int N = sc.nextInt();
            sc.nextLine();
            String[] db = new String[N];
            for (int i = 0; i < N; i++) {
                db[i] = sc.next();
            }
            sc.nextLine();
            int q = sc.nextInt();
            sc.nextLine();
            String[] queries = new String[q];
            for (int i = 0; i < q; i++) {
                queries[i] = sc.next();
            }
            int[] res = noOfSteps(N, db, q, queries);
            for (int i : res) {
                System.out.println(i);
            }
        }

    }

}