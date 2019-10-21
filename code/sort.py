# sorting for objects based off of arbitrary comparators

def m_sort(list_of_objs, size, comparator):
	assert(size >= 1)
	if size == 1:
		return list_of_objs
	else:
		mid = size//2
		right = list_of_objs[:mid]
		left = list_of_objs[mid:]
	
	m_sort(left, mid, comparator) # split
	m_sort(right, size - mid, comparator)
	
	l_size = len(left)
	r_size = len(right)
	i = j = k = 0
	
	# sublist sort
	while i < l_size and j < r_size:
		l_val = left[i]
		r_val = right[j]
		# pass the minimum of the two to the final list using
		# a custom comparator

		next_val = comparator(l_val, r_val)
		if next_val == l_val:
			list_of_objs[k] = l_val
			i += 1
		else:
			list_of_objs[k] = r_val
			j += 1
		k += 1

	#merge
	while i < l_size:
		list_of_objs[k] = left[i]
		i += 1
		k += 1

	while j < r_size: 
		list_of_objs[k] = right[j]
		j += 1
		k += 1

	return list_of_objs

# default int comparator for ints, mergesort
def int_min(val_1, val_2):
	if val_1 < val_2:
		return val_1
	else:
		return val_2

	
