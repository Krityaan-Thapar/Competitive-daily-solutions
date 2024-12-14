import java.util.*;

class BTreeNode<T> {
    public T data;
    public BTreeNode<T> left;
    public BTreeNode<T> right;

    BTreeNode(T data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class NTreeNode<T> {
    public T data;
    public ArrayList<NTreeNode<T>> child;

    NTreeNode(T data) {
        this.data = data;
        child = new ArrayList<NTreeNode<T>>();
    }
}

public class Solution {
    public static BTreeNode<Integer> encode(NTreeNode<Integer> root) {
        if (root == null) {
            return null;
        }

        BTreeNode<Integer> encoded = new BTreeNode<Integer>(root.data);
        if (root.child.size() > 0) {
            encoded.left = encode(root.child.get(0));
        }

        BTreeNode<Integer> curr = encoded.left;
        for (int i = 1; i < root.child.size(); i++) {
            curr.right = encode(root.child.get(i));
            curr = curr.right;
        }
        return encoded;
    }

    public static NTreeNode<Integer> decode(BTreeNode<Integer> root) {
        if (root == null) {
            return null;
        }

        NTreeNode<Integer> decoded = new NTreeNode<Integer>(root.data);
        BTreeNode<Integer> curr = root.left;
        while (curr != null) {
            decoded.child.add(decode(curr));
            curr = curr.right;
        }
        return decoded;
    }
}