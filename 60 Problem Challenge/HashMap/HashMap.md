HashMap 

set_val(key, value)
	inserts key value pair, if value already exist, update it
get_val(key)
	returns val given key
delete_val(key)
	removes mapping for the specific key

class HashTable:
	def __init__(self, size):
		this.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range (self.size()]
	def set_val(self, key, val):
		
