# current operations are push, pop, min_heap, max_heap, show_heap.

class heap:
    def __init__(self):
        self.heap=[]

    # Heap push operation.
    # append to the last of heap and perform ShiftDown operation to balance heap.
    def h_push(self,key):
        self.heap.append(key)
        self.shift_down_min(self.heap,0,len(self.heap)-1)

    # Heap pop operation
    # pop the first element of heap. and replace  with the last elememt.
    # perform a ShiftUp to balance heap.
    def h_pop(self):
        last_item=self.heap.pop()
        if self.heap:
            node = self.heap[0]
            self.heap[0]=last_item
            self.shift_up_max(self.heap,0)
            return node
        return last_item


    # ShiftDown operation to heapify the heap.
    # Results into min heap
    def shift_down_min(self,heap,start,pos):
        newchild = heap[pos]
        while pos > start:
            parent_index = (pos-1)>>1
            parent = heap[parent_index]
            if newchild < parent:
                heap[pos] = parent
                pos = parent_index
                continue
            break
        heap[pos] = newchild

    # ShiftDown operation to heapify the heap.
    # Results into max heap
    def shift_down_max(self,heap,start,pos):
        newchild = heap[pos]
        while pos > start:
            parent_index = (pos-1)>>1
            parent = heap[parent_index]
            if newchild > parent:
                heap[pos] = parent
                pos = parent_index
                continue
            break
        heap[pos] = newchild

    # ShiftUp operation to heapify the heap.
    # Results into max heap
    def shift_up_max(self,heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        childpos = 2*pos + 1   
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        heap[pos] = newitem
        self.shift_down_min(heap, startpos, pos)

    # ShiftDown operation to heapify the heap.
    # Results into min heap
    def shift_up_min(self,heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        childpos = 2*pos + 1   
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not heap[rightpos] < heap[childpos]:
                childpos = rightpos
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        heap[pos] = newitem
        self.shift_down_min(heap, startpos, pos)

    # Print the heap
    def show(self):
        print(self.heap)
