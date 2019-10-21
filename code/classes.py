# CS340 Project Classes Implementation
# Russell Rivera
# 10/19/2019


"""
Redo pointer implementation, and then redo all of this that you just did
"""




class Professor(object):
	
	# contains keys, which when put into a dictionary of classes or timeslots
	# returns the object of that class or timeslot
	def __init__(self, key_c1, key_c2, key_ts1, key_ts2):
		self.cl_1 = key_c1
		self.cl_2 = key_c2
		self.ts_1 = key_ts1
		self.ts_2 = key_ts2


class Student(object):

	# preference list is just a list
	def __init__(self, name, pref_list): #next_student
		self.name = name
		self.prefs = pref_list


class Timeslot(object):
	
	def __init__(self, rms_available, list_of_rooms):
		self.rooms =  list_of_rooms # list sorted in smallest to largest order by size 
		self.open = rms_available
		# where index of next room is self.open - 1

class Room(object):
		
	def __init__(self, size, next_room):
		self.size = size
		self.courses = []

	# change the size of a room 
	def ch_size(self, step):
		self.size += step

	def set_course(self, course_name):
		self.courses.append(course_name)

class Course(object):
	
	def __init__(self, popul, studs, teacher, room, ts):
		self.popl = popul
		self.teacher = teacher
		self.students = studs	
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
