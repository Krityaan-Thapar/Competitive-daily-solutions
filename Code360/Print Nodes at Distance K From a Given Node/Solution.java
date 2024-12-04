import java.util.List;
import java.util.ArrayList;

class BinaryTreeNode<T> {
    T data;
    BinaryTreeNode<T> left;
    BinaryTreeNode<T> right;
    BinaryTreeNode(T data) {
        this.data = data;
        left = null; right = null;
    }
}

public class Solution {
    public static void subtreeAdd(BinaryTreeNode<Integer> node, int dist, int maxmDist,
            List<BinaryTreeNode<Integer>> sol) {
        if (node == null) {
            return;
        }

        if (dist == maxmDist) {
            sol.add(node);
        } else {
            subtreeAdd(node.left, dist + 1, maxmDist, sol);
            subtreeAdd(node.right, dist + 1, maxmDist, sol);
        }
    }

    public static int dfs(BinaryTreeNode<Integer> root, BinaryTreeNode<Integer> target, int K,
            List<BinaryTreeNode<Integer>> sol) {
        if (root == null) {
            return -1;
        } else if (root == target) {
            subtreeAdd(root, 0, K, sol);
            return 1;
        } else {
            int L = dfs(root.left, target, K, sol);
            int R = dfs(root.right, target, K, sol);

            if (L != -1) {
                if (L == K) {
                    sol.add(root);
                }

                subtreeAdd(root.right, L + 1, K, sol);
                return L + 1;
            } else if (R != -1) {
                if (R == K) {
                    sol.add(root);
                }

                subtreeAdd(root.left, R + 1, K, sol);
                return R + 1;
            } else {
                return -1;
            }
        }
    }

    public static void dfsHelper(BinaryTreeNode<Integer> root, BinaryTreeNode<Integer> target, int K,
            List<BinaryTreeNode<Integer>> sol) {
        int temp = dfs(root, target, K, sol);
    }

    public static List<BinaryTreeNode<Integer>> printNodesAtDistanceK(BinaryTreeNode<Integer> root,
            BinaryTreeNode<Integer> target, int K) {
        List<BinaryTreeNode<Integer>> sol = new ArrayList<>();
        sol.clear();
        dfsHelper(root, target, K, sol);
        return sol;
    }
}