import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np # type: ignore
import random
from time import perf_counter

sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN: int = 10000


def example_graph_creation() -> None:
    # Return log-base-2 of 'x' + 5.
    def f_to_graph(x: float) -> float:
        return math.log2(x) + 5.0

    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords: List[float] = [float(i) for i in range(1, 100)]
    y_coords: List[float] = [f_to_graph(x) for x in x_coords]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label="log_2(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend()  # makes the 'label's show up
    plt.show()

def random_tree(val: int) -> BinarySearchTree:
    bst = BinarySearchTree(lambda x, y: x < y, None)
    for _ in range(val):
        bst = insert(bst, random.random())
    return bst

def height(node: Node | None) -> int:
    if node == None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def average_tree_height() -> None:
    print("Working...")
    n_max = 50
    x_coords = [i+1 for i in range(n_max)]
    y_coords = []
    for x in x_coords:
        heights = 0
        for _ in range(TREES_PER_RUN):
            bst = random_tree(x)
            heights += height(bst.root)
        y_coords.append(heights / TREES_PER_RUN)
    # Plotting the average heights
    x_numpy = np.array(x_coords)
    y_numpy = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label="Average Height")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Height")
    plt.title("Average Height of Random BSTs")
    plt.grid(True)
    plt.legend()
    plt.show()

def insert_random_value() -> None:
    print("Working...")
    n_max = 40
    x_coords = [i+1 for i in range(n_max)]
    y_coords = []
    for x in x_coords:
        times = 0
        for _ in range(TREES_PER_RUN):
            value = random.random()
            bst = random_tree(x)
            start_time = perf_counter()
            bst = insert(bst, value)
            end_time = perf_counter()
            times += end_time - start_time
        y_coords.append(times / TREES_PER_RUN)
        #Plotting average times
    x_numpy = np.array(x_coords)
    y_numpy = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label="Average Insertion Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Time (seconds)")
    plt.title("Average Insertion Time for Random Values in BSTs")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    #average_tree_height()
    insert_random_value()
    '''
    n_max = 40
    start = perf_counter()
    for _ in range(TREES_PER_RUN):
        value = random.random()
        bst = random_tree(n_max)

        bst = insert(bst, value)
    end = perf_counter()
    print(f"Inserted {TREES_PER_RUN} random values into BSTs in {end - start} seconds.")
    #average_tree_height()
    '''
    '''
    n_max = 50
    start = perf_counter()
    for _ in range(TREES_PER_RUN):
        bst = random_tree(n_max)
        bst_height = height(bst.root)
    end = perf_counter()
    print(f"Generated {TREES_PER_RUN} trees and calculated their heights in {end - start} seconds.")
    #example_graph_creation()
    '''
