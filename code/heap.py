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
		

	def _heapify_up(self, child_index):
		heap, compare = self.heap, self.compare
		while child_index > 0:
			child = heap[child_index]
			parent = heap[child_index // 2]
			if child < parent:
				return
			parent, child = child, parent				

	def _heapify_down 
