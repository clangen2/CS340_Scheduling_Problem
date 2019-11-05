from classes import *


#O(num_resouces)
def score_match(Course, Room):
    score = 0
    for i in range(len(Course.requirements)):
        if Course.requirements[i] == Room.resources[i]:
            score += 1
    return score *50 #class room resources are very important, and should be better for overall score than enrolling more students


def find_best_room_for_course(Course, Rooms):
    max_score, max_room = 0, ""
    for Room in Rooms:
        if max_score < score_match(Course, Room):
            max_score = score_match(Course, Room)
            max_room = Room
        #print(max_room)
    return max_score, max_room
