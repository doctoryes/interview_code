# Determine if a string has all unique characters. Don't use additional data structures.

from collections import defaultdict

def all_unique_characters_1(s):
	"""
	"""
	chars = defaultdict(int)
	for char in s:
		chars[char] += 1
	for char in chars.items():
		if char[1] > 1:
			return False
	return True

def all_unique_characters_2(s):
	"""
	"""
	chars = {}
	for char in s:
		if char in chars:
			return False
		chars[char] = 1
	return True

assert(all_unique_characters_1('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
assert(not all_unique_characters_1('The quick brown fox jumps over the lazy dog".'))
assert(not all_unique_characters_1('aa'))
assert(all_unique_characters_2('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
assert(not all_unique_characters_2('The quick brown fox jumps over the lazy dog".'))
assert(not all_unique_characters_2('aa'))