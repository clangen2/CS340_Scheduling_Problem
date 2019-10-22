from classes import *

# read the constraints file, parse data by lines, return a list of strings,
# where each line is a separate string
def read_const_data(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()
	return lines


# given the number of rooms, create a list of room objects, initialized with size
# and a name (integer value), returns a list of room objs sorted by room size
def build_room_objs(num_rooms, lines):
	room_objs = []
	for i in range(2, num_rooms + 2):
		#parse rooms and room sizes
		room_and_size = lines[i]
		room_name = room_and_size[0]
		room_size = int(room_and_size[1:-1])
		
		new_room = Room(room_name, room_size)
		room_objs.append(new_room)

	room_objs.sort()
	return room_objs	


# given the number of timeslots and the list of sorted rooms, create list
# of timeslot objects
def build_ts_objs(num_ts, room_objs):
	ts_objs = [] 
	for i in range(1, num_timeslots): 
		new_ts_obj = Timeslot(i, room_objs)
		ts_objs.append(new_ts_obj)
	return ts_objs		


# given the number of courses, produce a list of unique course objects
def build_course_objs(num_courses):
	course_objs = []
	for i in range(1, num_courses+1):
		new_course_obj = Course(i)
		course_objs.append(new_course_obj)
	return course_objs


# given the number of courses, produce a dictionary of professor objects
# for each pair of professors and classes given, set the class attributes
# for the professors. Return the list of set professor objs
def build_prof_objs(num_courses, pairs, Courses):
	Professors = []
	prof_dct = {}
	for i in range(1, (num_courses//2)+1):
		new_prof = Professor(i)
		prof_dct[i] = new_prof

	pairs = process_pairs(pairs)
	for pair in pairs:
		course = int(pair[0])
		prof = int(pair[1])
		
		prof_obj = prof_dct[prof]
		cl = Courses[course-1] 
		prof_obj.set_cl(cl)
	for obj in prof_dct.values():
		Professors.append(obj)
	
	return Professors
	

#parse pairwise information in a constraint or reference file, helper for 
# build_prof_objs
def process_pairs(list_of_pairs):
	split_p = []
	for pair in list_of_pairs:
		pairs = pair.split()
		split_p.append(pairs)
	return split_p


# build the main thingy
if __name__ == '__main__':

	lines = read_const_data('test.txt')
	
	#parse number of time_slots and number of rooms from all data
	num_timeslots = int(lines[0][-2])
	num_rooms = int(lines[1][-2])
	num_courses = int(lines[2 + num_rooms][-2])
	
	#parse professor - course pairs
	prof_and_courses = lines[4 + num_rooms:]

	#build main lists
	Rooms = build_room_objs(num_rooms, lines) #O(num_rooms)
	Timeslots = build_ts_objs(num_timeslots, Rooms) #O(num_timeslots)
	Courses = build_course_objs(num_courses) #O(num_courses)
	Professors = build_prof_objs(num_courses, prof_and_courses, Courses) #O(2*num_courses) 
	Students = 
	

	print(Rooms)
	print('\n')	
	print(Timeslots)
	print('\n')
	print(Courses)
	print('\n')
	print(Professors)