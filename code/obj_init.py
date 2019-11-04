from classes import *
import random

# CS340 Scheduling Problem
# Russell Rivera, Alton Wiggers, Carter Langen, Andy Hong
# obj_init.py
# File to initialize all objects for the main algorithm


# read data from constaint and preference files
def read_data(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()
	return lines

# given the number of rooms, and room and roomsize pairs from const data,
# build a sorted list of room objects initialized with room name/number and size
def build_room_objs(num_rooms, const_data):
	room_objs = []
	for i in range(2, num_rooms + 2):
		#parse rooms and room sizes
		room_and_size = const_data[i]
		room_and_size = room_and_size.split()
		room_name = int(room_and_size[0])
		room_size = int(room_and_size[1])

		new_room = Room(room_name, room_size)
		room_objs.append(new_room)

	room_objs.sort()
	return room_objs

# given the number of timeslots and a list of room objects, build a list of
# timeslot objects initialized with a name, and a pointer to a sorted list of rooms
# objects
def build_ts_objs(num_ts, num_s, room_objs):
	ts_objs = []
	for i in range(0, num_ts):
		new_ts_obj = Timeslot(i, room_objs)
		for j in range(0, num_s):
			new_ts_obj.students[j] = False
		ts_objs.append(new_ts_obj)
	return ts_objs

# given a list of courses, build a sorted list of course objects initiliazed
# with name only
def build_course_objs(num_courses):
	course_objs = []
	for i in range(1, num_courses + 1):
		new_course_obj = Course(i, random.randint(0,4))
		course_objs.append(new_course_obj)
	return course_objs

# given the number of courses, a list of professor course pairs, and a list of
# course objects, produce a list of professor objects, initialized pointers to
# corresponding course objects
def build_prof_objs(num_courses, pairs, Courses):
	Professors = []
	prof_dct = {}
	for i in range(1, (num_courses // 2) + 1):
		new_prof = Professor(i)
		prof_dct[i] = new_prof

	pairs = process_pairs(pairs)
	for pair in pairs:
		course = int(pair[0])
		prof = int(pair[1])

		prof_obj = prof_dct[prof]
		course_obj = Courses[course - 1]
		p_val = prof_obj.set_cl(course_obj)
		c_val = course_obj.set_prof(prof_obj)
		assert(p_val != False and c_val != False)

	for obj in prof_dct.values():
		Professors.append(obj)

	return Professors

# given a the student preference file, parse the input to find the number
# of students, for each student, create an object initialized by name and
# preference list, where preference list is a list of integers corresponding
# to the name of an course name (number)
def build_student_objs(num_students, list_of_students):
	Students = []
	for i in range(0, num_students):
		# parse the list of pairs
		student_pref_pair = list_of_students[i].split('\t')
		student_i = int(student_pref_pair[0])
		pref_list = student_pref_pair[1].split()
		pref_list = list(map(int, pref_list))

		new_student = Student(student_i, pref_list, random.randint(0,4))
		Students.append(new_student)
	return Students

# given a list of students objects, update course popularities for each object
def course_popularities(Courses, Students, majorPrefsExt):
	majorDesire = 0 #value of total major classes wanted by major students
	for student in Students:
		for course in student.prefs: # constant search (only 4 classes)
			course_num = int(course) - 1 #index of course i in Courses
			Courses[course_num].increment_popl() #increase popularity
			#put majors at the front of the list
			if majorPrefsExt and student.major == Courses[course_num].department:
				Courses[course_num].students.insert(0, student.name)
				majorDesire +=1
			else:
				Courses[course_num].students.append(student.name) #add student to list
	return majorDesire

# helper function for parsing during building professor objects
def process_pairs(list_of_pairs):
	split_p = []
	for pair in list_of_pairs:
		pairs = pair.split()
		split_p.append(pairs)
	return split_p

# build and initialize all lists required to run the algorithm
def build_all_objs(constraints_file, preference_file, majorPrefsExt):
	"""
	This function does the following things:
	Create: (1) a list of room objects sorted by size, with name, size attributes full
		(2) a list of timeslot objects with a pointer to a list of room objects
		(3) a list of courses objects initialized with name and professor object
		(4) a list of students objects initialized with a name and preference list
			note: preference list is not a list of objects, it is a list of
			names of objects, where names are integers.
		(5) a list of professor objects sorted by popularity, initialized with name and
			a two pointers to class objects
	Return: (1..5)
	"""
	#open the constraint file and the prefrence_list file
	lines = read_data(constraints_file)
	preference_lists = read_data(preference_file)
	#parse data from files to feed to functions
	num_timeslots = int(lines[0].split('\t')[1][:-1])
	# parse data for number of rooms
	num_rooms = int(lines[1][6:-1])
	#print(int(lines[1][6:-1]))
	num_courses = int(lines[2 + num_rooms][8:-1])
	#print(lines[2 + num_rooms][8:-1])
	prof_and_courses = lines[4 + num_rooms:] # parse professor course pairs
	#print(lines[4 + num_rooms:])
	num_students = int(preference_lists[0].split('\t')[1][:-1]) # parse number of students
	#print(preference_lists[0].split('\t')[1][:-1])
	student_prefs = preference_lists[1:] # parse student preference pairs
	#print(preference_lists[1:])

	# build lists
	Rooms = build_room_objs(num_rooms, lines) #O(num_rooms * log(num_rooms)
	Timeslots = build_ts_objs(num_timeslots,num_students, Rooms) #O(num_timeslots)
	Students = build_student_objs(num_students, student_prefs) #O(num_students)
	Courses = build_course_objs(num_courses) #O(num_courses)
	majorDesire = course_popularities(Courses, Students, majorPrefsExt) #O(num_students)
	Professors = build_prof_objs(num_courses, prof_and_courses, Courses) #O(2*num_courses)
	Professors = sorted(Professors, reverse=True) #(O(num_profs *log(num_profs))

	return Rooms, Timeslots, Students, Courses, Professors, majorDesire
