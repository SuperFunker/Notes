class HashMap:
  # Initialise with array_size
  def __init__(self, array_size):
    self.array_size = array_size
    # Set all items to None
    self.array = [None for item in range(array_size)]

  # Create Hash Function // count_collisions set to 0 as default, will be used only when needed
  def hash(self, key, count_collisions=0):
    # Function that encodes the key to bytes
    key_bytes = key.encode()
    # Function that sums the key's bytes
    hash_code = sum(key_bytes)
    # Returns the hash_code, plus the collisions counter if needed
    return hash_code + count_collisions

  # Function used to compress hash_code and create array_index
  def compressor(self, hash_code):
    # Returns hash_code % array_size
    return hash_code % self.array_size

  # Function to assign item to hash_map
  def assign(self, key, value):
    # create array index with compressor and hash function using the key
    array_index = self.compressor(self.hash(key))
    # set the current key,pair value from the index in a variable (current_array_value OR cav for tutorial usage where cav[0] is the key and cav[1] the value)
    current_array_value = self.array[array_index]
    # If the current is empty, set it to key, value
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    # If current has same key, overwrite value
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # If the if above fails then there is collision
    # Set count_collisions = 1, to increment later in case of another collision
    number_collisions = 1
    # while current key is different to our key
    while(current_array_value[0] != key):
      # Crete new hash code with count_collisions
      new_hash_code = self.hash(key, number_collisions)
      # create new index by compressing new hash code
      new_array_index = self.compressor(new_hash_code)
      # set new current
      current_array_value = self.array[new_array_index]

      # If new current is empty, save key, value
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      # If new current has same key as our key, overwrite current
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      # If none of the above, increment collisions so that while repeats with new hash_code
      number_collisions += 1
    # When current has same key as ours while ends so we return
    return

  # Create Retrive value function
  def retrieve(self, key):
    # >> >> Same as assign function >> >> 
    array_index = self.compressor(self.hash(key))
    # >> >> Same as assign function >> >> 
    possible_return_value = self.array[array_index]

    # If key points to empty value, return None 
    if possible_return_value is None:
      return None

    # If return key is our key, return the value
    if possible_return_value[0] == key:
      return possible_return_value[1]
    
    # If none of the above, create collision index
    retrieval_collisions = 1

    # While return key
    while (possible_return_value != key): # Question *** Does it need possible_return_value[0] != key ???
      # Create new hash code with collision index
      new_hash_code = self.hash(key, retrieval_collisions)
      # Compress new hash code to get new index
      retrieving_array_index = self.compressor(new_hash_code)
      # return value = array[new_index]
      possible_return_value = self.array[retrieving_array_index]

      # If new return value is empty, return None
      if possible_return_value is None:
        return None

      # If return value key is same as our key, return value
      if possible_return_value[0] == key:
        return possible_return_value[1]

      # If none of the above, increment collision index to create new hash code in next while loop
      retrieval_collisions += 1
    # If value returned exit while loop
    return

# EXAMPLE
hash_map = HashMap(15)
hash_map.assign("gabbro","igneous")
hash_map.assign("sandstone","sedimentary")
hash_map.assign("gneiss","metamorphic")
print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))
