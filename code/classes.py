# CS340 Project Classes Implementation
# Russell Rivera
# 10/19/2019


class Professor(object):

	# name is the number designated to a teacher, c1, c2 are the names
	# of class objects
	def __init__(self, name):
		self.name = name
		self.cl_1 = None
		self.cl_2 = None
		self.ts_1 = None
		self.ts_2 = None

	def set_ts1(self, time):
		self.ts_1 = time

	def set_ts2(self, time):
		if self.ts_1 != time:
			self.ts_2 = time
			return 0 #valid
		else:
			return -1 #invalid timeslot, should never happen

	def set_cl(self, course):
		if self.cl_1 == None:
			self.cl_1 = course
		self.cl_2 = course

	# return popularity, defined by the sum of the popularity (popl)
	# of the two classes
	def get_pop(self):
		if self.cl_1 and self.cl_2:
			popl = self.cl_1.popl + self.cl_2.popl
			return popl
		else:
			return 0

	# comparison based off of popularity
	def __lt__(self, other):
		return self.get_pop() < other.get_pop()

	def __gt__(self, other):
		return self.get_pop() > other.get_pop()

	def __le__(self, other):
		return self.get_pop() <= other.get_pop()

	def __ge__(self, other):
		return self.get_pop() >= other.get_pop()

	def __eq__(self, other):
		return self.get_pop() == other.get_pop()

	def __ne__(self, other):
		return self.get_pop() != other.get_pop()

	def __repr__(self):
		course_1 = str(self.cl_1)
		course_2 = str(self.cl_2)
		name = str(self.name)
		return 'Professor: ' + name + ' c1: ' + course_1 + ' c2: '+ course_2

class Student(object):


	def __init__(self, name, pref_list): #next_student
		self.name = name
		self.prefs = pref_list #list of four courses by name
		self.courses = [] #list of enrolled courses
		self.enrolled = 0

	def enroll(self, course):
		self.courses.append(course)
		self.enrolled += 1

	# constant time at worst 4 lookups
	def is_preference(self, course):
		return course in self.prefs

	def __repr__(self):
		return "Student: " + str(self.name) + " prefrences " + str(self.prefs)


class Timeslot(object):

	def __init__(self, name, rooms):
		self.name = name
		self.rooms = rooms
		self.open = len(rooms)

	def close_room(self):
		if (self.open - 1) >= 0:
			self.open -= 1
		else:
			return -1 #invalid, all rooms in self.rooms have been used

	def __eq__(self, other):
		return self.name == other.name

	def __repr__(self):
		return str(('Timeslot ' + str(self.name), \
		'Rooms: ' + str(self.rooms), \
		'open slots: ' + str(self.open)))

class Room(object):

	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.courses = set()


	def set_course(self, course_name):
		self.courses.add(course_name)



	# comparison suite for Room objects
	def __lt__(self, other):
		return self.size < other.size

	def __gt__(self, other):
		return self.size > other.size

	def __le__(self, other):
		return self.size <= other.size

	def __ge__(self, other):
		return self.size >= other.size

	def __eq__(self, other):
		if type(self) == type(other):
			return self.size == other.size
		return False

	def __ne__(self, other):
		return self.size != other.size

	def __repr__(self):
		return str((self.size, self.size, self.courses))

class Course(object):

	def __init__(self, name):
		self.name = name
		self.prof = None
		self.popl = 0 #num of students that want to take the class
		self.time = None #when course is taught
		self.room = None #what room class is taught

	def increment_popl(self):
		self.popl += 1

	# time is the name of a tiimeslot object
	def set_time(self, time_obj):
		self.time = time_obj

	# room is the name of a room object
	def set_room(self, room_obj):
		self.room = room_obj


	# comparison suite for Course objects
	def __lt__(self, other):
		return self.popl < other.popl

	def __gt__(self, other):
		return self.popl > other.popl

	def __le__(self, other):
		return self.popl <= other.popl

	def __ge__(self, other):
		return self.popl >= other.popl

	def __eq__(self, other):
		if type(self) == type(other):
			return self.popl == other.popl
		return False

	def __ne__(self, other):
		return self.popl != other.popl

	def __repr__(self):
		return str(self.name)
