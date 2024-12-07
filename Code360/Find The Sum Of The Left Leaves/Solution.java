class TreeNode<T> {
	public T data;
	public TreeNode<T> left;
	public TreeNode<T> right;

	TreeNode(T data) {
	    this.data = data;
	    left = null;
	    right = null;
	}
}

public class Solution {
    public static int sumOfLeftLeaves(TreeNode<Integer> root) {
        return dfs(root, false);
    }

	public static int dfs(TreeNode<Integer> curr, boolean isLeft) {
		if (curr.left == null && curr.right == null) {
			if (isLeft) {	
				return curr.data;
			} else {
				return 0;
			}
		}
		int left = 0, right = 0;
		if (curr.left != null) {
			left = dfs(curr.left, true);
		}
		if (curr.right != null) {
			right = dfs(curr.right, false); 
		}
		return left + right;
	}
}