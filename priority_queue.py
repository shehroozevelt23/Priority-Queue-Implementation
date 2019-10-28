from binary_tree import *

class PriorityQueue:
  ''' Fields: _heap '''
  
  # PriorityQueue() produces an empty Priority Queue 
  # __init__: None -> PriorityQueue 
  def __init__(self):
    self._heap = BinaryTree()
  
  # self.is_empty() returns a boolean value based on whether or not self is empty 
  # is_empty: PriorityQueue -> Bool 
  def is_empty(self):
    if self._heap.is_empty() == True:
      return True 
    else:
      return False
  
  # self.lookup_min() returns pair containing the minimum key in self 
  # lookup_min: PriorityQueue -> Pair 
  def lookup_min(self):
    return self._heap._A[0]
  
  # self.add(key, element) adds pair containing key & element to self 
  # add: PriorityQueue Any Any -> None 
  # Effects: Mutates self to contain pair containing key & element 
  def add(self, key, element):
    last = self._heap.next_leaf()
    self._heap.add_last(key, element)
    curr = last 
    par = self._heap.get_parent(curr)
    while par != -1 and self._heap.get_key(curr) < self._heap.get_key(par):
      self._heap.swap_node_values(curr, par)
      curr = par 
      par = self._heap.get_parent(curr) 
   
  # self.delete_min() deletes the pair with minimum key from self 
  # delete: PriorityQueue -> Pair 
  # Effects: Mutates self to not contain pair with the minimum key 
  def delete_min(self):
    root = self._heap.get_root()
    min_key = self._heap._A[root].get_key()
    min_element = self._heap._A[root].get_element()
    last = self._heap.get_last()
    self._heap.swap_node_values(root, last) 
    self._heap.delete_last()
    last = self._heap.previous_leaf()
    curr = root 
    left = self._heap.get_left(curr)
    right = self._heap.get_right(curr)
    key = self._heap.get_key(curr) 
    stop = False 
    while left != False and not stop:
      min_child = left 
      if self._heap._A[left] == None and self._heap._A[right] == None:
        break
      if right != False and self._heap._A[right].get_key() < self._heap._A[left].get_key():
        min_child = right
      if self._heap.get_key(min_child) < key:
        self._heap.swap_node_values(curr, min_child)
        curr = min_child 
        left = self._heap.get_left(curr)
        right = self._heap.get_right(curr)
      else:
        stop = True 
      
    p = Pair(min_key, min_element)
    return p
    
    
