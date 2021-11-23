# Node Class
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

# Double Linked List Class
class DoublyLinkedList:
  # create head / tail nodes
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  # Adds node to head
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    #Checks if list not empty
    if current_head != None:
      #If not empty set new before current and current after new
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    # if list empty insert new
    self.head_node = new_head
    # if list has no tail
    if self.tail_node == None:
      #new tail = head
      self.tail_node = new_head
  # Adds node to tail (Same as above)
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail
  # Removes the head of the list
  def remove_head(self):
    # save head you want to remove
    removed_head = self.head_node
    #If no head then empty list
    if removed_head == None:
      return None
    #Assign node after head node as head node
    self.head_node = removed_head.get_next_node()
    # if head node exists
    if self.head_node != None:
      #Remove previous link to node
      self.head_node.set_prev_node(None)
    # if the removed variable is self.tail
    if removed_head == self.tail_node:
      #remove list tail
      self.remove_tail()

    return removed_head.get_value()
  # Removes the tail of the list (same as above)
  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()
  # Removes a node in the list based on its value
  def remove_by_value(self, value_to_remove):
    #Create node to remove / set current node as the head (used as a start to go through the list)
    node_to_remove = None
    current_node = self.head_node
    # While Node list hasnt ended
    while current_node != None:
      # If the nodes value is the same as the value we are looking to remove
      if current_node.get_value() == value_to_remove:
        # Set node_to_remove variable as the current node
        node_to_remove = current_node
        # Exit loop
        break
      #go to next node
      current_node = current_node.get_next_node()
    # If there isnt a value matching
    if node_to_remove == None:
      # End with no result
      return None
    # If the node we want to remove is self.head_node
    if node_to_remove == self.head_node:
      # Remove head node
      self.remove_head()
    # If the node we want to remove is self.tail_node
    elif node_to_remove == self.tail_node:
      # Remove tail node
      self.remove_tail()
    # If node in between
    else:
      # Set next_node as the node after the node we want removed
      next_node = node_to_remove.get_next_node()
      # Set prev_node as the node before the node we want removed
      prev_node = node_to_remove.get_prev_node()
      # Set nexts node previous node to prev_node
      next_node.set_prev_node(prev_node)
      # Set previous node next node to next_node
      prev_node.set_next_node(next_node)
    # Return the node we removed
    return node_to_remove
  # Prints List
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

