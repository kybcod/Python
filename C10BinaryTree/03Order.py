class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
        
    def insert_lef(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree
    
    #전위이동        
    def preorder(tree):
        if tree:
            print(tree.key)
            preorder(tree.left_child)
            preorder(tree.right_child)
    
    #후위이동        
    def postorder(tree):
        if tree:
            postorder(tree.left_child)
            postorder(tree.right_child)
            print(tree.key)
    
    #중위이동        
    def inorder(tree):
        if tree:
            inorder(tree.left_child)
            print(tree.key)
            inorder(tree.right_child)