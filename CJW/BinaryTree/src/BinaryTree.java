class Node {
    int data;
    Node leftChild;
    Node rightChild;

    public Node(int data) {
        this.data = data;
        this.leftChild = this.rightChild = null;
    }
}


public class BinaryTree {

    public Node insertNode(Node root, int data) {
        if(root == null) {
            return new Node(data);
        }

        if(data < root.data) {
            root.leftChild = insertNode(root.leftChild, data);
        }
        else {
            root.rightChild = insertNode(root.rightChild, data);
        }
        return root;
    }

    public Node searchNode(Node root, int searchtarget) {
        if(root == null) {
            return null;
        }

        if(root.data == searchtarget){
            return root;
        }
        else if(searchtarget < root.data){
            return searchNode(root.leftChild, searchtarget);
        }
        else {
            return searchNode(root.rightChild, searchtarget);
        }
    }

    public Node deleteNode(Node root, int deletetarget) {
        if(root == null) {
            return null;
        }

        if(deletetarget < root.data) {
            root.leftChild = deleteNode(root.leftChild, deletetarget);
        }
        else if(deletetarget > root.data) {
            root.rightChild = deleteNode(root.rightChild, deletetarget);
        }
        return root;
    }

    //전위순회
    public void preorder(Node currentNode) {
        if(currentNode != null) {
            System.out.println(currentNode.data + " ");
            preorder(currentNode.leftChild);
            preorder(currentNode.rightChild);
        }
    }
    //중위순회
    public void inorder(Node currentNode) {
        if(currentNode != null) {
            inorder(currentNode.leftChild);
            System.out.println(currentNode.data + " ");
            inorder(currentNode.rightChild);
        }
    }
    //후위순회
    public void postorder(Node currentNode) {
        if(currentNode != null) {
            postorder(currentNode.leftChild);
            postorder(currentNode.rightChild);
            System.out.println(currentNode.data + " ");
        }
    }

}
