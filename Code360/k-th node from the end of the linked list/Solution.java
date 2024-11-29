class Node {
    int data;
    Node next;

    Node(int val) {
        this.data = val;
        this.next = null;
    }
}

public class Solution {
    static Node ans;
    public static Node findKthFromLast(Node head, int k) {
        recurse(head, k);
        return ans;
    }

    public static int recurse(Node curr, int k) {
        if(curr == null) {
            return 0;
        }
        
        int v = recurse(curr.next, k) + 1;
        if (v == k) {
            ans = curr;
        }
        return v;
    }
}