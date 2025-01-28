class LinkedListNode {
    public int data;
    public LinkedListNode next;

    LinkedListNode(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Solution {
    public static LinkedListNode mergeInBetween(int x, int y, LinkedListNode head1, LinkedListNode head2) {
		LinkedListNode tail = head2;
        while (tail.next != null) {
            tail = tail.next;
        }

        LinkedListNode pre_x = head1;
        LinkedListNode post_y = head1;
        while (y > -1) {
            if (x == 1) {
                pre_x = post_y;
            }
            x--;
            y--;
            post_y = post_y.next;
        }
        pre_x.next = head2;
        tail.next = post_y;
        return head1;
	}
}
