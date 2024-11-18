class Node {
    public int data;
    public Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Solution{
	public static Node modifyLL(Node head){
		if (head == null || head.next == null) {
            return head;
        }
        Node ans = head;
        Node slow = head;
        Node fast = head;
        Node fPrev = null;
        while (fast != null && fast.next != null) {
            fPrev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        fPrev.next = null;

        Node prev = null;
        Node curr = slow;
        Node next = null;
        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        Node head1 = head;
        Node head2 = prev;
        Node head1Next = head1.next;
        Node head2Next = head2.next;
        Node aux = head1;

        while (head1 != null && head2 != null) {
            aux = head2;
            head1Next = head1.next;
            head2Next = head2.next;
            head1.next = head2;
            head2.next = head1Next;
            head1 = head1Next;
            head2 = head2Next;
        }

        if (head2 !=null) {
            aux.next = head2;
        }
        
        return ans;
	}
}