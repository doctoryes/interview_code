

# Given an image represented by a N x N matrix, where each pixel is represented by an integer,
# rotate it 90 degrees in-place.

from enum import Enum
import pprint

class Direction(Enum):
	LEFT = 1
	RIGHT = 2


def rotate(image, direction):
	"""
	Params:
		image: Two-dimensional array of integers.
	Returns rotated image.
	"""
	# pprint.pprint(image)
	dim = len(image[0])
	if direction == Direction.LEFT:
		for x in range(0, dim):
			for y in range(0, x):
				# print(f"image[{y}][{x}] <=> image[{x}][{y}]")
				temp = image[y][x]
				image[y][x] = image[x][y]
				image[x][y] = temp
	elif direction == Direction.RIGHT:
		for x in range(0, dim):
			for y in range(0, dim - 1 - x):
				# print(f"image[{x}][{y}] <=> image[{dim-1-y}][{dim-1-x}]")
				temp = image[x][y]
				image[x][y] = image[dim-1-y][dim-1-x]
				image[dim-1-y][dim-1-x] = temp

	# pprint.pprint(image)
	return image


assert(rotate([[1,1,1],[2,2,2],[3,3,3]], Direction.LEFT) == [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
assert(rotate([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], Direction.LEFT) == [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
assert(rotate([[1,1,1],[2,2,2],[3,3,3]], Direction.RIGHT) == [[3, 2, 1], [3, 2, 1], [3, 2, 1]])
assert(rotate([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], Direction.RIGHT) == [[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]])

