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

@dataclass(frozen=True)
class BinarySearchTree:
    def comes_before()
        pass
    tree : BinTree

def is_empty(bst : BinarySearchTree):
    if bst.tree is None:
        return True
    return False

def insert(bst : BinarySearchTree, value : Any):
    if comes_before(value, bst):
        
