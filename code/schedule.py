from classes import *
from obj_init import *
# import heap

# write this
def schedule():
	pass

if __name__ == '__main__':
	
	constraints = 'constraints_test.txt'
	student_pref = 'pref_test.txt'

	Rooms, Timeslots, Students, Courses, Professors = build_all_objs(constraints, student_pref)

	'''
	Rooms is a list of ROOM OBJECTS sorted by size 
	Timeslots is a list of TIMESLOT OBJECTS that is SORTED by name (1..n)
	Students is a list of STUDENT OBJECTS sorted by name (1..n) 
	Courses is a list of COURSE OBJECTS sorted by name (1..n)
	Professors is a list of PROFESSOR OBJECTS sorted by popularity,
		where popularity is the sum of the students that want
		to enroll in both of that professor's classes.
	'''

	'''
	PLEASE READ OBJ_INIT to see which attributes are already initialized.
	Professors and classes are already attributes of each other, but not
	much else is. Please make sure you do not update an attribute 
	unnecessarily.
	
	I have not implemented the heap yet, but I cannot do any more today,
	I am confident you can figure out the rest with what I have. 

	-R  
	'''

	print(Rooms)
	print(Timeslots)
	print(Courses)
	print(Professors)
	print(Students)
