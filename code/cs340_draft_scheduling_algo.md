```
Class Professor:

		def __init__(self, list_courses):
				self.courses = list_courses

Class Course:
	
		def __init__(self, prof):
				self.professor = prof
				self.students = {} # keyed by student name, T/F
				self.time = None
				self.student_pq = None
				self.room = None
				
		def add_student(self, student):
				self.students[student] = True
		
		def set_time(self, time):
				self.time = time
		
		def set_pq(self, array_heap):
				self.student_pq = array_heap
				
		def set_room(self, room):
				self.room = room
				
		#optional getters

Class Student:

		def __init__(self, name, pref_list):
				self.name = name
				self.pref = pref_list
				self.courses = [] or {} # preference here, bound at 4, so constant lookup
			
		def add_course(self, course):
				self.courses.append(course)
				

Class Room:

		def __init__(self, size):
				self.size = size
				self.timeslots = [] # will have to fill every timeslot for each room anyway
				# list of pointers to objs
	
		def get_size(self):
				return self.size
				
		def get_ts(self):
				return self.timeslots

Class Timeslot:

		def __init__(self):
				self.rooms = {}
		
		def add_room(self, room_obj):
				self.rooms[room] = room_obj # or pointer to room obj

Auxilary Data Structures:

Dictionary of Dictionaries for seeing if a professor is available.
Dictionary of Dictionaries for seeing if a student is available.



A) Initialize a list of Professor objects with courses = list_of_profs
B) Initialize a list of Course objects, sorted by popularity = sorted_courses
C) Initialize a list of Room objects, sorted by size = sorted_rooms


```

