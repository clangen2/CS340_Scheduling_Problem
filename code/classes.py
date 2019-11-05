# CS340 Scheduling Problem
# Russell Rivera, Alton Wiggers, Carter Langen, Andy Hong
# classes.py
# File of all classes used

class Professor(object):

	# name is the number designated to a teacher, c1, c2 are
	# the names of (pointers to) class objects
	# note: ts_1 corresponds to cl_1, etc
	def __init__(self, name):
		self.name = name
		self.cl_1 = None
		self.cl_2 = None
		self.ts_1 = None
		self.ts_2 = None

	# set a timeslot attribute, if both courses are full, return
	# False, there is an invalid scheduling, if ts_1 full, then
	# add to ts_2 attribute
	def set_ts(self, time_obj):
		if self.ts_1 and self.ts_2:
			return False
		else:
			if self.ts_1:
				self.ts_2 = time_obj
			self.ts_1 = time_obj
		return True

	# set a course, if cl_1 = course 1 is full, then add to the
	# cl_2 attribute
	def set_cl(self, course_obj):
		if self.cl_1 and self.cl_2:
			return False
		else:
			if self.cl_1:
				self.cl_2 = course_obj
			else:
				self.cl_1 = course_obj
		return True

	def get_pop(self):
		if self.cl_1.popl and self.cl_2.popl:
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
		return 'Professor ' + str(self.name)


class Student(object):

	def __init__(self, name, pref_list, major=None, classYear=None): #next_student
		self.name = name
		self.prefs = pref_list #list of four courses by name
		self.courses_taken = [] #list of enrolled courses (objs)
		self.enrolled = 0 #number of courses student is enrolled in
		self.major = major #student major
		self.classYear = classYear #class year

	# add a course obj to courses list (list of enrolled courses)
	def enroll_in(self, course_obj):
		self.courses_taken.append(course_obj)
		self.enrolled += 1

	# constant time at worst 4 lookups
	def is_preference(self, course_obj):
		return course_obj.name in self.prefs

	def __repr__(self):
		return 'Student ' + str(self.name)


class Timeslot(object):

	def __init__(self, name, list_of_room_objs):
		self.name = name
		self.rooms = list_of_room_objs
		self.open = len(list_of_room_objs)
		self.students = {}

	def close_room(self):
		if (self.open - 1) >= 0:
			self.open -= 1
		else:
			print("assigned to empty timeslot")
			return False
			 #invalid all rooms in self.rooms used

	def __eq__(self, other):
		if other == None:
			return False
		else:
			return self.name == other.name

	def __repr__(self):
		return 'Timeslot ' + str(self.name)


class Room(object):

	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.courses = set()

	def set_course(self, course):
		self.courses.add(course)

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
		return 'Room ' + str(self.name)


class Course(object):

	def __init__(self, name, num_section = 1, section = 1, department=None):
		self.name = str(name) #should be a string
		self.prof = None
		self.popl = 0 #num students that want to take the class
		self.students = [] #list of students in the class
		self.enrollment = 0 #num students enrolled
		self.time = None #when course is taught
		self.room = None #what room class is taught
		self.department = department #department of the class
		self.section= section
		self.num_section= num_section
		self.quorum=0
		self.popularity_index=0

	def set_popularity_index(self):
		if self.num_section==1:
			self.popularity_index=0
		else:
			self.popularity_index=1
	
	def set_quorum(self):
		self.quorum=self.prof.cl_2.popl

	def split(self):
		self.num_section +=1
		self.popularity_index +=1
		self.prof.cl_2 = Course(self.name + " B", 2, 2) #reset the prof's 2nd class to be the 2nd section of the class
		self.prof.cl_2.set_popularity_index()
		
	def need_split(self):
		#check if the course need to split / should only be called after room has been assigned
		if self.num_section==2:
			print("already 2 sections, no need to split")
			return False
		if self.room:
			if self.popl> (self.room.size+self.quorum):
				return True
			else:
				return False


	def increment_popl(self):
		self.popl += 1

	def increment_enroll(self):
		self.enrollment += 1

	# time is the name of a tiimeslot object
	def set_time(self, time_obj):
		self.time = time_obj

	# room is the name of a room object
	def set_room(self, room_obj):
		self.room = room_obj

	# professor is a professor obj
	def set_prof(self, professor_obj):
		self.prof = professor_obj

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
		return 'Course ' + str(self.name)
