# **Python_cheatsheet_and_classes**
**Python cheatsheet, predefined functions and classes**

[**Python Cheatsheet**](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

## Sorting Class
A class for sorting functions (currently: bubble, insertion, count, merge and quick) 
**How to use**
* Copy *sorting_class.py* into working directory.
* Import sorting class
```
from sorting_class import sorting_algo 
```
* Make class object
```
sort_obj = sorting_algo()
```
* Pass the list to the functions. return will be a sorted list.
```
sorted_list = sort_obj.bubble_sort(list)
sorted_list = sort_obj.insertion_sort(list)
sorted_list = sort_obj.count_sort(list)
sorted_list = sort_obj.merge_sort(list)
sorted_list = sort_obj.quick_sort(list)
```
* Use meta function to check list items and size.
```
sorted_list = sort_obj.meta(list)
```
## Binary Search Tree Class
A class for BST functions (currently: insertion, deletion, traversal, find_min, find_max) 
**How to use**
* Copy *bst_class.py* into working directory.
* Import bst class
```
from bst_class import bst 
```
* Make class object
```
tree = bst()
```
* Operations on tree
```
tree.insert(value)
tree.traversal()
tree.delete(value)
min = tree.find_min()
max = tree.find_max()
```