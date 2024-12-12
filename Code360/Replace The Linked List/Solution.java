class Node {
    public int data;
    public Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Solution {
    public static Node replaceWithSum(Node head) {
        Node ans = head;
        Node curr = null;
        int sum = 0;

        while (head != null) {
            if (head.data == 0) {
                if (sum == 0) {
                    head = head.next;
                    ans = head;
                    continue;
                }

                if (curr == null) {
                    ans = head;
                    curr = ans;
                } else {
                    curr.next = head;
                    curr = head;
                }
                curr.data = sum;
                sum = 0;
            } else {
                sum += head.data;
            }
            head = head.next;
        }

        if (ans == null) {
            return new Node(0);
        }
        return ans;
    }
}