
############
##
## Bubble sort
##
############
# Order: O(N^2)
#
def bubble_sort(list):
	"""
	Bubble-sorts a list in-place.
	"""
	for i in range(0, len(list)):
		for j in range(0, len(list)):
			if list[i] < list[j]:
				tmp = list[i]
				list[i] = list[j]
				list[j] = tmp
	return list


############
##
## Merge sort
##
############

# Order: O(N log N)
#
def _merge(arr, left, mid, right):
	"""
	Merge the array elements from left to mid and mid to right as sorted in-place.
	"""
	# Calculate how many values to sort on left and right.
	num_l_vals = mid - left + 1
	num_r_vals = right - mid

	# Make temporary left/right sliced arrays of current values.
	l_arr = arr[left:left + num_l_vals]
	r_arr = arr[mid + 1:mid + num_r_vals + 1]

	# Compare the l/r arrays element-by-element and sort elements in the original list.
	num_l_sorted = 0
	num_r_sorted = 0
	curr_idx = left
	while (num_l_sorted < num_l_vals and num_r_sorted < num_r_vals):
		if l_arr[num_l_sorted] <= r_arr[num_r_sorted]:
			arr[curr_idx] = l_arr[num_l_sorted]
			num_l_sorted += 1
		else:
			arr[curr_idx] = r_arr[num_r_sorted]
			num_r_sorted += 1
		curr_idx += 1

	# Copy over any remaining l/r elements.
	while (num_l_sorted < num_l_vals):
		arr[curr_idx] = l_arr[num_l_sorted]
		num_l_sorted += 1
		curr_idx += 1
	while (num_r_sorted < num_r_vals):
		arr[curr_idx] = r_arr[num_r_sorted]
		num_r_sorted += 1
		curr_idx += 1

def _merge_sort(arr, left, right):
	if right > left:
		mid = (right - left) // 2 + left
		_merge_sort(arr, left, mid)
		_merge_sort(arr, mid + 1, right)
		_merge(arr, left, mid, right)

def merge_sort(arr):
	_merge_sort(arr, 0, len(arr) - 1)
	return arr


############
##
## Quick sort
##
############

# Order: O(N log N)
#
def _swap(arr, idx1, idx2):
	"""
	Swaps the values at the two indices in the array in-place.
	"""
	if idx1 == idx2:
		# No need to swap the same value.
		return
	tmp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = tmp

def _partition(arr, low, high):
	"""
	Divides array into two paritions around pivot point.
	All the numbers to the left of the pivot point will be less than the pivot number.
	All the numbers to the right of the pivot point will be greater than the pivot number.
	"""
	pivot_val = arr[high]
	pivot_idx = low - 1
	for j in range(low, high):
		# Is the current element less than or equal to the pivot?
		if arr[j] <= pivot_val:
			# Move the pivot index forward.
			pivot_idx += 1
			# Swap the current element with the element at the temporary pivot index.
			_swap(arr, pivot_idx, j)

	# Move the pivot element to the correct pivot position
	# (between the smaller and larger elements).
	pivot_idx += 1

	# Swap pivot element with high element.
	_swap(arr, pivot_idx, high)

	# Return the pivot element.
	return pivot_idx

def _quicksort(arr, low, high):
	"""
	Sorts a (portion of an) array, divides it into partitions, then sorts those partitions.
	"""
	if low >= high or low < 0:
		return

	# Partition the array and get the pivot index.
	pivot_idx = _partition(arr, low, high)

	# Sort the two partitions.
	_quicksort(arr, low, pivot_idx - 1)
	_quicksort(arr, pivot_idx + 1, high)

def quick_sort(arr):
	_quicksort(arr, 0, len(arr) - 1)
	return arr


############
##
## Insertion sort
##
############

# Order: O(N^2)
#
def insertion_sort(arr):
	"""
	Like sorting a hand of cards.
	Start at the left + 1.
	If the value is less than before, shift all values to the right and insert it.
	O(n^2)
	"""
	idx = 1
	while idx < len(arr):
		val = arr[idx]
		i = idx - 1
		while i >= 0 and val < arr[i]:
			arr[i + 1] = arr[i]
			i -= 1
		arr[i + 1] = val
		idx += 1
	return arr


