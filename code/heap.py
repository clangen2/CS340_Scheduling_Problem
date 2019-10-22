from classes import Timeslot

class Heap(object):

	# array representation of a min heap
	def __init__(self, heap=None, compare=operator.lt):
		if heap == None:
			self.heap = []
		self.heap = heap
		self.size = len(heap)
		self.compare = compare

	def _insert(self, item):
		self.heap.append(item)
		self.heapify_up()
		

	def _heapify_up(self, index):
		while index > 1:
			child = self.heap[index]
			parent = self.heap[index//2]
			if child < parent:
				
				
			

	def _heapify_down 
