# Binary Search Trees

## The runway problem

There is a single runway in an airport. We want to schedule plane landings in an optimistic fashion so that each landing maintains a threshold of K minutes with it's adjacent ones.

Its an optimization problem we want to address with the data-structures that we already know.

Given the size of the Set `R` is `n`; We have to meet these expectations in `O(log(n))`:

 1. Search for a specific landing
 1. Remove an already landed flight
 1. Insert a new landing in an optimum manner

### Unsorted array

Problem: anything we want to do that match the expectaitons is, at best, `O(n)`

### Sorted array

- searching is `log n`
- comparing is `O(1)`
- inserting is `O(n)`: needs shifting

### Heap (min/max heap)
- finding element that is <= k or >= k is `O(n)`

## The Binary Search Tree

Is actually a tree with pointers and stuff.

```python
{
    'key'           : 'some value',
    'parent'        : 'POINTER',
    'left_child'    : 'POINTER',
    'right_child'   : 'POINTER'
}
```

**Invarient**: for each node `x`
 * if `y` is in the left _subtree_ of `x` we must have: `key(y) <= key(x)`
 * if `y` is in the right _subtree_ of `x` we must have: `key(y) >= key(x)`

### Inserting:
49, 79, 46, 41

if `h` is the hight if the tree, insertions are `O(h)`

### Augmented BST
Add subtree size of 1 or more to each node