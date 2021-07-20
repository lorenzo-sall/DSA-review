from binarytree import *

r = BinaryTree('a')
print(r.get_root())
print(r.get_lchild())
r.ins_l('b')
r.ins_r('c')
r.ins_l('b')
r.ins_r('c')

r.ins_l('b')
r.ins_l('b')
r.ins_l('b')

print(r.get_lchild())
print(r.get_lchild().get_root())
print(r.get_rchild())
print(r.get_rchild().get_root())
r.get_rchild().set_root('test')
print(r.get_rchild().get_root())


print(f"height: {r.find_height()}")
