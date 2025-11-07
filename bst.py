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
    def insert_helper(node: BinTree, value: Any) -> BinTree:
        #if the node is none insert a new node
        if node is None:
            return Node(value, None, None)
        
        #compare using comes before function
        if bst.comes_before(value, node.value):
            #value is smaller, insert to the left
            return Node(node.value, insert_helper(node.left, value), node.right)
        else:
            #value is larger or equal, insert to right
            return Node(node.value, node.left, insert_helper(node.right, value))
        
    if is_empty(bst):
        #if tree is empty, create new tree
        return BinarySearchTree(bst.comes_before, Node(value, None, None))
    
    #recurse
    new_tree = insert_helper(bst.tree, value)
    return BinarySearchTree(bst.comes_before, new_tree)

def lookup(bst: BinarySearchTree, value: Any) -> bool:
    def lookup_helper(node: BinTree) -> bool:
        if node is None:
            return False
        
        #check if the value is equal to the current nodes value
        if not bst.comes_before(value, node.value) and not bst.comes_before(node.value, value):
            return True
        
        #if the value is smaller, search left subtree
        elif bst.comes_before(value, node.value):
            return lookup_helper(node.left)
        
        #if the value is larger, search right subtree
        else:
            return lookup_helper(node.right)
        
    return lookup_helper(bst.tree)
        
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

    def test_lookup(self):
        bst = BinarySearchTree(compare_value, None)
        bst = insert(bst, 10)
        bst = insert(bst, 5)
        bst = insert(bst, 15)
        empty_bst = BinarySearchTree(compare_value, None)

        self.assertEqual(lookup(bst, 10), True)
        self.assertEqual(lookup(bst, 5), True)
        self.assertEqual(lookup(bst, 15), True)

        self.assertEqual(lookup(bst, 8), False)

        self.assertEqual(lookup(empty_bst, 10), False)
        
if __name__ == "__main__":
    unittest.main()