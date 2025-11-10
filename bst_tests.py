import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 
from bst import * 
class BSTTests(unittest.TestCase): 
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
 
if (__name__ == '__main__'): 
    unittest.main()
