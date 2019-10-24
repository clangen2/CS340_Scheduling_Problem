from classes import *
from obj_init import *
# import heap

def schedule(constraints, student_pref, output_file):
	# constraints = 'constraints.txt'
	# student_pref = 'student_prefs.txt'
	# output_file = 'schedule.out'

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
	slotNum = 0
	slotMax = len(Timeslots)

	for professor in Professors:
		slot = Timeslots[slotNum]
		professor.set_ts(slot)
		cl = professor.cl_1
		cl.set_time(slot)
		cl.set_room(slot.rooms[slot.open - 1])
		slot.close_room()
		slotNum += 1
		if slotNum >= slotMax:
			slotNum = 0

		slot = Timeslots[slotNum]
		professor.set_ts(slot)
		cl = professor.cl_2
		cl.set_time(slot)
		cl.set_room(slot.rooms[slot.open - 1])
		slot.close_room()
		slotNum += 1
		if slotNum >= slotMax:
			slotNum = 0

	output = []
	for i in range(len(Courses)+1):
		if i==0:
			header_str="Course\tRoom\tTeacher\tTime\tStudents"
			output.append(header_str)
		else:
			output.append(str(Courses[i-1].name))
			output[i] += "\t" + str(Courses[i-1].room.name)
			output[i] += "\t" + str(Courses[i-1].prof.name)
			output[i] += "\t" + str(Courses[i-1].time.name) + "\t"

	for student in Students:
		for i in range(3):
			conflict = False
			for j in range(len(student.courses_taken)):
				if Courses[student.prefs[i] - 1].time == Courses[student.courses_taken[j] - 1].time:
					conflict = True
			if Courses[student.prefs[i] - 1].enrollment >= Courses[student.prefs[i] - 1].room.size:
				conflict = True
			if not conflict:
				student.enroll_in(student.prefs[i])
				Courses[student.prefs[i] - 1].increment_enroll()
				output[student.prefs[i]] += str(student.name) + " "

	outString = ""
	for i in range(len(output)):
		outString += output[i] + "\n"

	f = open(output_file,"w+")
	f.write(outString)
	f.close()
