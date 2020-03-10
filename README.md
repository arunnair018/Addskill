# **Python_cheatsheet_and_classes**
**Python cheatsheet, predefined functions and classes**

[**Python Cheatsheet**](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

## Sorting Class
---
A class for sorting functions (currently: bubble, insertion, count, merge and quick) 
**How to use**
* Copy *sorting_class.py* into working directory.
* Import sorting class
```from sorting_class import sorting_algo ```
* Make class object
```sort_obj = sorting_algo()```
* Pass the list to the functions. return will be a sorted list.
```sorted_list = sort_obj.bubble_sort(list)```
```sorted_list = sort_obj.insertion_sort(list)```
```sorted_list = sort_obj.count_sort(list)```
```sorted_list = sort_obj.merge_sort(list)```
```sorted_list = sort_obj.quick_sort(list)```
* Use meta function to check list items and size.
```sorted_list = sort_obj.meta(list)```