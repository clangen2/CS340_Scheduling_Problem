from classes import *
from obj_init import *
from functions_for_room_extentions import *

class Schedule():


	def __init__(self, constraints, student_pref, output_file):

		'''
		Rooms is a list of ROOM OBJECTS sorted by size
		Timeslots is a list of TIMESLOT OBJECTS that is SORTED by name (1..n)
		Students is a list of STUDENT OBJECTS sorted by name (1..n)
		Courses is a list of COURSE OBJECTS sorted by name (1..n)
		Professors is a list of PROFESSOR OBJECTS sorted by popularity,
			where popularity is the sum of the students that want
			to enroll in both of that professor's classes.
		'''
		#extensions enabled
		self.majorPrefsExt = False #major preferences
		self.room_resources = True #room_resources
		#extension values
		self.majorEnrollment = [0,0] #how many students were enrolled in major classes and how many students wanted major classes


		self.num_resouces = 5
		self.room_score = 0
		#initialize lists
		self.Rooms, self.Timeslots, self.Students, self.Courses, self.Professors,self.majorEnrollment[1] = build_all_objs(constraints, student_pref, self.majorPrefsExt, self.num_resouces)

		for professor in self.Professors:
			#assign timeslots and rooms for both classes
			self.assignSlot(professor.cl_1, None)
			self.assignSlot(professor.cl_2, professor.cl_1.time)

		#format output
		output = []
		for i in range(len(self.Courses) + 1):
			if i == 0:
				header_str="Course\tRoom\tTeacher\tTime\tStudents"
				output.append(header_str)
			else:
				output.append(str(self.Courses[i - 1].name))
				output[i] += "\t" + str(self.Courses[i - 1].room.name)
				output[i] += "\t" + str(self.Courses[i - 1].prof.name)
				output[i] += "\t" + str(self.Courses[i - 1].time.name) + "\t"
				for j in range(self.Courses[i - 1].enrollment):
					output[i] += str(self.Courses[i - 1].students[j]) + " "

		outString = ""
		for i in range(len(output)):
			outString += output[i] + "\n"
		f = open(output_file,"w+")
		f.write(outString)
		f.close()

		if self.majorPrefsExt:
			print("Major Satisfaction: " + str(self.majorEnrollment[0]) + "/" + str(self.majorEnrollment[1]))
		if self.room_resources:
			print("Room Resources Satisfaction " + str(self.room_score))

	# assigns a course to a timeslot and a room, enrolls students in the course
	def assignSlot(self, cl, badTime):
		#print(cl)
		slot = None
		openRooms = 0
		compatibility = 0
		compatibleStuds = []
		for time in self.Timeslots:
			#check if professor is already teaching
			if time != badTime:
				#immediately choose a timeslot if it has more open rooms than others checked
				if time.open > openRooms:
					openRooms = time.open
					compatibility,compatibleStuds = self.checkCompatibility(time, cl)

					slot = time
					openRooms = time.open
				#if equal rooms to other times checked, compare compatibility
				elif time.open == openRooms:
					newComp,newStuds = self.checkCompatibility(time, cl)
					if newComp > compatibility:
						compatibility = newComp
						compatibleStuds = newStuds
						slot = time
						openRooms = time.open
		#set timeslot
		cl.set_time(slot)
		available = slot.open_rooms()
		bestroom = available[-1] #biggest room available at timeslot
		#determine the resousce-bestroom in time slot
		if self.room_resources:
			score, room = find_best_room_for_course(cl, available)
			if score + room.size > bestroom.size:
				#print(room.size)
				#print(bestroom.size)
				bestroom = room

		bestroom_index = available.index(bestroom)
		cl.set_room(slot.rooms[bestroom_index])
		slot.close_room(bestroom_index)
		slot.open_rooms()
		cl.students = []
		for student in compatibleStuds:
			conflict = False
			for j in range(len(self.Students[student - 1].courses_taken)):
				if self.Courses[self.Students[student - 1].courses_taken[j].name - 1].time == slot:
					conflict = True
			if not conflict and not cl.enrollment >= bestroom.size:
				#print(cl.enrollment, " ", bestroom.size, bestroom)
				self.Students[student - 1].enroll_in(cl)
				cl.students.append(student)
				cl.enrollment +=1
				if self.room_resources:
					self.room_score += score
				if self.majorPrefsExt and cl.department == self.Students[student - 1].major:
					self.majorEnrollment[0] += 1



	# generate a list of compatible students
	def checkCompatibility(self,time, cl):
		compatibility = 0
		compatibleStuds = []
		for student in cl.students:
			#check if student is potentially assigned to that timeslot
			if not time.students[student - 1]:
				compatibility += 1
				compatibleStuds.append(student)
		return compatibility, compatibleStuds


	# main scheduling algorithm
