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

	for professor in Professors:
		#assign timeslots and rooms for both classes
		assignSlot(professor.cl_1, None, Timeslots)

		assignSlot(professor.cl_2, professor.cl_1.time, Timeslots)

	#format output
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
		#for each preferred class
		for i in range(3):
			conflict = False
			#do not enroll if conflicts with already enrolled classes
			for j in range(len(student.courses_taken)):
				if Courses[student.prefs[i] - 1].time == Courses[student.courses_taken[j] - 1].time:
					conflict = True
			#do not enroll if class is full
			if Courses[student.prefs[i] - 1].enrollment >= Courses[student.prefs[i] - 1].room.size:
				conflict = True
			if not conflict:
				#add class to enrolled classes
				student.enroll_in(student.prefs[i])
				Courses[student.prefs[i] - 1].increment_enroll()
				#add to output file
				output[student.prefs[i]] += str(student.name) + " "

	outString = ""
	for i in range(len(output)):
		outString += output[i] + "\n"

	f = open(output_file,"w+")
	f.write(outString)
	f.close()

def assignSlot(cl, badTime, Timeslots):
	slot = None
	openRooms = 0
	compatibility = 0
	compatibleStuds = []
	for time in Timeslots:
		#check if professor is already teaching
		if not time == badTime:
			#immediately choose a timeslot if it has more open rooms than others checked
			if time.open > openRooms:
				openRooms = time.open
				compatibility,compatibleStuds = checkCompatibility(time, cl)
				slot = time
				openRooms = time.open
				#if equal rooms to other times checked, compare compatibility
			elif time.open == openRooms:
				newComp,newStuds = checkCompatibility(time, cl)
				if newComp > compatibility:
					compatibility = newComp
					compatibleStuds = newStuds
					slot = time
					openRooms = time.open
	#set timeslot
	cl.set_time(slot)
	cl.set_room(slot.rooms[slot.open - 1])
	slot.close_room()


def checkCompatibility(time, cl):
	compatibility = 0
	compatibleStuds = []
	for student in cl.students:
		#check if student is potentially assigned to that timeslot
		if not time.students[student - 1]:
			compatibility += 1
			compatibleStuds.append(student)
	return compatibility,compatibleStuds
