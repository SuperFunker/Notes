#from node
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
#Initialize Stack
class Stack:
  def __init__(self, limit=1000):
    #Set Top
    self.top_item = None
    #set size (empty on start)
    self.size = 0
    #set limit
    self.limit = limit
  # Add item to top of the list
  def push(self, value):
    # if limit > size
    if self.has_space():
      #Create Node with value
      item = Node(value)
      # Set value node next item the current top_item
      item.set_next_node(self.top_item)
      # Set stacks top_item as item
      self.top_item = item
      # Increment Stacks size by 1
      self.size += 1
    # If limit < Size
    else:
      print("All out of Space !")     
    
  #Remove Top of the Stack
  def pop(self):
    # If self.size != 0
    if not self.is_empty():
      #Create node remove_ that is the top_item
      item_to_remove = self.top_item
      #Set top_item as the node after the top_item
      self.top_item = item_to_remove.get_next_node()
      #Decrease size by 1
      self.size -= 1
      # Return the value of the removed item
      return item_to_remove.get_value()
    # If self.size = 0
    else:
      print("This stack is totally empty.")
  #See top_items value
  def peek(self):
    # If self.size > 0
    if not self.is_empty():
        # Returns the value
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  #Bool that compares the limit and the size
  def has_space(self):
    return self.limit > self.size
  #Bool that checks if the stack is empty
  def is_empty(self):
    if self.size == 0:
      return True
    return False