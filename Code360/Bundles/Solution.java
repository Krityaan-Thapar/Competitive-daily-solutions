import java.util.ArrayList;

class TrieNode {
    public TrieNode[] children = new TrieNode[26];
    public int count;

    TrieNode() {
        count = 0;

        for (int i = 0; i < 26; i++) {
            children[i] = null;
        }
    }
}

public class Solution {
    public static void insert(String s, TrieNode head) {
        TrieNode temp = head;
        for (char i : s.toCharArray()) {
            if (temp.children[i - 'a'] == null) {
                temp.children[i - 'a'] = new TrieNode();
            }
            temp = temp.children[i - 'a'];
            temp.count++;
        }
    }

    private static int countPrefix(TrieNode curr, int k) {
        if (curr == null) {
            return 0;
        }
        int contribution = (curr.count / k);
        for (int i = 0; i < 26; i++) {
            contribution = contribution + countPrefix(curr.children[i], k);
        }
        return contribution;
    }

    public static int groupsOfK(ArrayList<String> strList, int k) {
        TrieNode head = new TrieNode();
        for (int i = 0; i < strList.size(); i++) {
            insert(strList.get(i), head);
        }
        int maxScore = countPrefix(head, k);
        return maxScore;
    }
}