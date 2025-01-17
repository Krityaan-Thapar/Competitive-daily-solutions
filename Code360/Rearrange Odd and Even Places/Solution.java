class Node {
	public int data;
	public Node next;

	Node() {
		this.data = 0;
		this.next = null;
	}

	Node(int data) {
		this.data = data;
		this.next = null;
	}
}

public class Solution {
	public static Node oddEvenList(Node head) {
		Node s_even = new Node(-1);
		Node s_odd = new Node(-1);
		Node curr_even = s_even;
		Node curr_odd = s_odd;
		int parity = 1;

		if (head == null) {
			return null;
		}

		while (head != null) {
			if (parity == 0) {
				curr_even.next = head;
				curr_even = curr_even.next;
			} else {
				curr_odd.next = head;
				curr_odd = curr_odd.next;
			}
			head = head.next;
			parity = (parity + 1) % 2;
		}
		curr_even.next = null;
		curr_odd.next = s_even.next;
		return s_odd.next;
	}
}