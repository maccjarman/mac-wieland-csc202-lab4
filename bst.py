import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 

BinTree : TypeAlias = Union["Node", None]

@dataclass
class Node:
    value : Any
    left : BinTree
    right : BinTree

@dataclass(frozen=True) #shouldn't be mutated
class BinarySearchTree:
    comes_before : Callable[[Any, Any], bool] #comparison function
    tree : BinTree #root of the node tree

#checks if the BinarySearchTree is empty
def is_empty(bst : BinarySearchTree):
    return bst.tree is None

def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    #helper function for recurse
    def helper(node: BinTree, value: Any) -> BinTree:
        #if the node is none insert a new node
        if node is None:
            return Node(value, None, None)
        
        #compare using comes before function
        if bst.comes_before(value, node.value):
            #value is smaller, insert to the left
            return Node(node.value, helper(node.left, value), node.right)
        else:
            #value is larger or equal, insert to right
            return Node(node.value, node.left, helper(node.right, value))
        
    if is_empty(bst):
        #if tree is empty, create new tree
        return BinarySearchTree(bst.comes_before, Node(value, None, None))
    
    #recurse
    new_tree = helper(bst.tree, value)
    return BinarySearchTree(bst.comes_before, new_tree)
        
#custom comparison function for integers for testing
def compare_value(a: Any, b: Any) -> bool:
    return a < b

class Test(unittest.TestCase):
    
    def test_is_empty(self):
        bst = BinarySearchTree(compare_value, None)
        self.assertEqual(is_empty(bst), True)
        non_empty_bst = BinarySearchTree(compare_value, Node(10, None, None))
        self.assertEqual(is_empty(non_empty_bst), False)

    def test_insert(self):
        bst = BinarySearchTree(compare_value, None)
        bst = insert(bst, 10)
        self.assertEqual(is_empty(bst), False)
        self.assertEqual(bst.tree.value, 10)

        bst = insert(bst, 5)
        self.assertEqual(bst.tree.left.value, 5)
        
        bst = insert(bst, 20)
        self.assertEqual(bst.tree.right.value, 20)

if __name__ == "__main__":
    unittest.main()