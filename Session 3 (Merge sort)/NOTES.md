# Sorting

## Applications
 - Trivial
   - phonebook
   - Median in an array
   - SEARCH !!!
 - Non-trivial
   - compression(!)
   - graphics (render - front 2 back -> sorted)


## Comparison function

You need to have some sort of comparision function in order to determine the order of two elements in regard of each other.

## Two sorting algs

* Insertion sort
  - O(N) comparisons
  - O(N) swaps
  - worst case => reversed!

* Binary-Insertion sort
  - Because a[0-i] is already sorted
  - O(log(n)) comparisons
  - O(N) swaps

* Merge sort
  - Devide and Conquer
  - Two phases
    - sort
    - merge (*)