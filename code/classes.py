# CS340 Project Classes Implementation
# Russell Rivera
# 10/19/2019

class Teacher(object):
	
	# teacher object, defined with two classes and two
	# time slots

	# consider also, instead of pointers to objects,
	# another kind of reference? is this needed?
	def __init__(self, class_1, class_2, ts_1, ts_2):
		self.cl_1 = ptr(class_1)
		self.cl_2 = ptr(class_2)
		self.ts_1 = ptr(ts_1)
		self.ts_2 = ptr(ts_2)


	# alternatively, we could code into the algorithm
	# when to update which class/timeslot
	# update a class for a teacher
	def set_class(self, cl, which):
		if which == 1:
			self.cl_1 = ptr(cl)
		else:
			self.cl_2 = ptr(cl)

	# set a timeslot for a teacher
	def set_ts(self, time, which):
		if which == 1:
			self.ts_1 = ptr(time)
		else:
			self.ts_2 = ptr(time)

class Student(object):
	
	# if we are going to have a linked list of students
	# shouldn't we include a .next attribute?
	def __init__(self, pref_list): #next_student
		self.p_list = pref_list
		#self.next = ptr(next_student)
		
		# are we defining preference list 
		# as a list of pointers to student
		# objects?

class Timeslot(object):
	
	# pointer to the head of a linked list of rooms
	def __init__(self, h_rooms_ll):
		self.rooms = ptr(h_rooms_ll)


class Room(object):
		
	def __init__(self, size, next_room):
		self.size = size
		self.next = ptr(next_room)

	# change the size of a room 
	def ch_size(self, step):
		self.size += step
	
	# update the next pointer of the linked list
	def ch_next(self, new_next):
		self.next = ptr(new_next)


class Class(object):
	
	def __init__(self, pop, studs, teacher, room, ts):
		self.popl = pop
		self.teacher = teacher
		self.students = studs	
		self.room = room
		self.time_sl = ts	
	
# alternatively, we could have dictionary in which we store
# the key of a pointer and the value of a pointer

# simulate pointers using a "reference" to an obj.
class ptr(object):

	def __init__(self, obj):
		self.ref = obj

	def get_r(self):
		return self.ref

	def set_r(self, obj):
		self.ref = obj

# define custom comparators for sorting 
def class_comp(class_1, class_2):
	if class_1.size < class_2.size:
		return class_1
	else:
		return class_2

def room_comp(room_1, room_2):
	if room_1.size < room_2.size:
		return room_1
	else:
		return room_2
