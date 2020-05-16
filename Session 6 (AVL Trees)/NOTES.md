# AVL Trees

We talked about BST and the attributes of a BST:

1. search is `O(lg(h))`
2. insert is `O(1)`
3. delete is `O(1)`

Define the **hight** of a **tree** as follows:
> the longest path from root to a leaf

Define the **hight** of a **node** as follows:
> the longest path from the node to a leaf

Define the depth of a node as follows:
> the level that the node is in the tree

## The Representation Invariant
The data in the DS is organized in a certain way and as long as the data is organized in that way, the DS functions correctly.

_e.g.: for a sorted array: each element should be >/< if it's next element_

as long as the RI holds, the DS returns correct result for the queries that are ran on it.

TIP: implement a method (e.g. `check_ri`) and call it on every update on the DS to make sure the RI holds.

## Augmented Data Structures
We talked about data structures being augmented with auxiliary information to facilitate further processes on the DS.

We can augment the BST with each node's hight to facilitate the AVL balacing algorithm.

## Attributes of an AVL tree

For every node the hight of left and right sub-trees must defer by at most 1

## Balancing a tree

what are the number of nodes in an AVL tree of hight `h`?

Assume `N<h>`be the minimum number of nodes in an AVL tree of height `h`.
using recursion we have:
* base case: `N<0>` = `O(1)`
* recursion: `N<h> = 1 + N<h-2> + N<h-1>`

so `N<h>` is bigger than **Fibonacci** series and we know that Fibonacci is exponential.

> Fibonacchi formula => `phi^h/sqrt(5)`

## Rotation

`left-rotate` and `right-rorate` so that the resulting tree when traversed **in-order** is equal to the original.