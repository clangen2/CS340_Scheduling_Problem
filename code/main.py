
import schedule
import sys

# import obj_init

def get_args():
	args = sys.argv
	constraints = args[1]
	student_prefs = args[2]
	output = args[3]
	return constraints, student_prefs, output

if __name__ == '__main__':

	c, s, o = get_args()
	schedule.schedule(c, s, o)
