/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        Stack<TreeNode> s = new Stack<TreeNode>();
        List<Integer> answer = new ArrayList<Integer>();
        
        //Initialize
       traverseLeft(s,root);
        
        while(!s.empty()){
            TreeNode currentNode = s.pop();
            answer.add(currentNode.val);
            
            if(currentNode.right != null){
                currentNode = currentNode.right;
                traverseLeft(s,currentNode);
            }
        }
        
        return answer;
    }
    
    private void traverseLeft(Stack s, TreeNode root){
        
         while(root != null){
            s.push(root);
            root = root.left;
        }
        
    }
}