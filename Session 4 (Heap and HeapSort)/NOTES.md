# Heaps

## Heaps as ADTs

## A little about stack/heap in OS vs. stack/heap the ADT

## Usages

### Priority Queue

Priority Queue is a set `S` of elements in which, each element is associated with a key.

### Operations
* `insert(S, x)`: insert element `x` into set `S`
* `max(S)`: return the element in `S` with the largest key
* `extract_max(S)`: `max(S)` + remove the element from `S`
* `increase_key(S,x,k)`: increase `x`'s key in set `S` to the new value `k`

 The heap is an implementation of priority queue which is an ARRAY! visualized as a nearly COMPLETE binary tree.

 |1|2|3|4|5|6|7|8|9|10|
 |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
 |16|14|10|8|7|9|3|2|4|1

* the root is first element (i=0)
* parent (i) = `i/2`
* left child = `2*i`
* right-child = `2*i + 1`

#### MAX_HEAP property
the key of a node is >= the key of its **children**

#### MIN_HEAP property
the key of a node is <= the key of its **children**

#### max_heapify
For node `i`, if the trees rooted at _left(i)_ and _right(i)_ are max-heaps we only have ONE violation. hence: corrects a **SINGLE** violation of a heap where left and right children are max-heaps already.

Complexity: **`O(log n)`** | _why?_

### Heap Sort