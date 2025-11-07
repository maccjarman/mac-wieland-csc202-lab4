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
        
def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def delete_helper(node: BinTree, value: Any) -> BinTree:
        if node is None:
            return None #if there's no value, there's nothing to delete
        
        #if the value to be deleted is smaller than the node's value, go to the left subtree
        if bst.comes_before(value, node.value):
            node.left = delete_helper(node.left, value)

        #if the value to be deleted is greater than the node's value, go to the right subtree
        elif bst.comes_before(node.value, value):
            node.right = delete_helper(node.right, value)

        #once we find the node to delete
        else:
            #leaf node
            if node.left is None and node.right is None:
                return None
            
            #node has one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            #node has two children
            else:
                #find smallest node in right subtree
                successor = find_min(node.right)

                #replace current node's value with successor's value
                node.value = successor.value
                
                #delete successor from right subtree
                node.right = delete_helper(node.right, successor.value)

        return node #return modified node
    
    def find_min(node: BinTree) -> Node:
        current = node
        while current and current.left != None:
            current = current.left
        return current
    
    new_tree = delete_helper(bst.tree, value)
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
        
    def test_delete(self):
        bst = BinarySearchTree(compare_value, None)
        bst = insert(bst, 10)
        bst = insert(bst, 5)
        bst = insert(bst, 15)
        bst = insert(bst, 3)
        bst = insert(bst, 7)

        #leaf node
        bst = delete(bst, 3)
        self.assertEqual(lookup(bst, 3), False)
        
        #one child
        bst = delete(bst, 7)
        self.assertEqual(lookup(bst, 7), False)


if __name__ == "__main__":
    unittest.main()