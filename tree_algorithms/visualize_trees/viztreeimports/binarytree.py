# Binary Tree structure with the class BinaryTree, implementing the following methods:
#  BinaryTree()         constructor
#  get_root()           get methods for root
#  get_lchild()             left child
#  get_rchild()             right child
#  set_root(value)      set method for root
#  ins_l(value)         insert left
#  ins_r(value)         insert child

class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.lc = None
        self.rc = None

    def get_root(self):
        return self.key

    def get_lchild(self):
        return self.lc

    def get_rchild(self):
        return self.rc

    def set_root(self, root):
        self.key = root

    def ins_l(self, new_node):
        if self.lc == None:                     # case with no left node present
            self.lc = BinaryTree(new_node)
        else:                                   # case wit a left node present. the existing subtree is pushed down one level
            inserted = BinaryTree(new_node)     # create new tree
            inserted.lc = self.lc               # set the current left subtree as the left child of the new tree
            self.lc = inserted                  # set the new subtree as the left subtree of the original node

    def ins_r(self, new_node):
        if self.rc == None:
            self.rc = BinaryTree(new_node)
        else:
            inserted = BinaryTree(new_node)
            inserted.rc = self.rc
            self.rc = inserted

    # return max of two values
    def max_h(self, hl, hr):
        if hl >= hr:
            return hl
        else:
            return hr

    # finds the height of the tree recursively. h = 0 if empty tree
    def find_height(self):
        h = 0
        if self.lc == None and self.rc == None:
                return h
        else:
            if self.lc == None:
                return self.rc.find_height() + 1
            elif self.rc == None:
                return self.lc.find_height() + 1
            else:
                return self.max_h(self.lc.find_height(), self.rc.find_height()) + 1
