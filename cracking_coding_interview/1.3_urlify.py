

def urlify(s):
	s_url_list = ['%20' if c == ' ' else c for c in s]
	return ''.join(s_url_list)


assert(urlify('Mr John Smith') == 'Mr%20John%20Smith')
