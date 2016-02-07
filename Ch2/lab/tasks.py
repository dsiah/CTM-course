from functools import reduce

# Vector Sum for lab
def add(v, w):
	if len(v) != len(w):
		raise TypeError

	return [x + y for (x, y) in zip(v, w)]

# Dot Product for lab
def dot(v, w):
	return sum([x * y for (x, y) in zip(v, w)])

# Task 2.12.1
def create_voting_dict(strlist):
	return {r[0]: [int(vote) for vote in r[3:]] for r in [l.split() for l in strlist]}

# Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
	return dot(voting_dict[sen_a], voting_dict[sen_b])

# Task 2.12.3
def most_similar(sen, voting_dict):
	vd = voting_dict
	#  Create a list of tuples of the senator and their dot with the input senator
	dots = [(osen, policy_compare(sen, osen, vd)) for osen in vd.keys() if osen != sen]

	# Return the max dot value (and corresponding senator's name)
	maxi = (None, float('-inf'))
	for tup in dots:
		if tup[1] > maxi[1]: 
			maxi = tup

	return maxi

# Variation on 2.12.3 but for any input list of the same length
def most_similar_to(inp, vd):
	dots = [(osen, dot(inp, vd[osen])) for osen in vd.keys()]
	# Return the max dot value (and corresponding senator's name)
	maxi = (None, float('-inf'))
	for tup in dots:
		if tup[1] > maxi[1]: 
			maxi = tup

	return maxi

# Task 2.12.4
def least_similar(sen, voting_dict):
	vd = voting_dict
	#  Create a list of tuples of the senator and their dot with the input senator
	dots = [(osen, policy_compare(sen, osen, vd)) for osen in vd.keys() if osen != sen]

	# Return the min dot value (and corresponding senator's name)
	mini = (None, float('inf'))
	for tup in dots:
		if tup[1] < mini[1]: 
			mini = tup
			
	return mini

# Task 2.12.6
def find_average_similarity(sen, sen_set, voting_dict):
	# Get a list of dots (senator dot-product with every other senator)
	sen_dots = [dot(voting_dict[sen], voting_dict[i]) for i in sen_set]
	# Return the sum of these dots divided by number of senators
	return sum(sen_dots) / len(sen_set) 

# Task 2.12.7
def find_average_record(sen_set, voting_dict):
	# Sum vectors using add vector function with reduction function and average
	return [i / len(sen_set) for i in reduce(add, [voting_dict[i] for i in sen_set])]

# Task 2.16.9
def bitter_rivals(voting_dict):
	vd, sens = voting_dict, list(voting_dict.keys())
	rivals   = (None, None, 41) # 40 is largest possible similarity

	for i in range(len(sens)):
		for j in range(i + 1, len(sens)):
			# Create tuple with the senators and their similarity index
			index = (sens[i], sens[j], policy_compare(sens[i], sens[j], vd))
			# Gets mininum between current rivals and current comparison
			# Lambda a: a[2] is a function that allows min to compare inner
			# tuple values
			rivals = min([rivals, index], key=lambda a: a[2])
	
	return rivals

if __name__ == '__main__':
	mylist = list(open('voting_record_dump109.txt')) # Open file into list form
	vd = create_voting_dict(mylist)                  # Creating Voting Dictionary
	
	# Cache democrats and republicans & all of them
	dems = [r[0] for r in [l.split() for l in mylist] if r[1] == 'D']
	reps = [r[0] for r in [l.split() for l in mylist] if r[1] == 'R']
	allp = [r[0] for r in [l.split() for l in mylist]]

	# Task 2.12.5
	csim = most_similar('Chafee', vd)
	print('Most similar senator to Chafee is {} with a score of {}'.format(csim[0], csim[1]))

	slsim = least_similar('Santorum', vd)
	print('Least similar senator to Santorum is {s[0]} with a score of {s[1]}'.format(s=slsim))

	# Task 2.12.6
	# Feinstein & Boxer Similarity index
	a, b  = 'Boxer', 'Feinstein'
	casim = policy_compare(a, b, vd)
	print('The similarity (index) between {} and {} is {}'.format(a, b, casim))

	# Task 2.12.6 & Task 2.12.8
	c = 'Allen' 
	dots_ave, dave = find_average_similarity(c, dems, vd), find_average_record(dems, vd) 

	print('Allen dotted with each D and then ave\'d yields {}'.format(dots_ave))
	print('The ave D voting record dotted with Allen yields {}'.format(dot(vd[c], dave)))

	# Everyone dotted with all dems - humorously unscalable

	sims = [(p, find_average_similarity(p, dems, vd)) for p in allp] 
	most_dem = max(sims, key=lambda a: a[1])

	print('Most Average D is {} with an (similarity) index of {}'.format(
		most_dem[0], most_dem[1]))

	dms = most_similar_to(dave, vd) # Most similar to the average Democratic voting
	print('Most Average D is {} with an (similarity) index of {}'.format(dms[0], dms[1]))

	# Task 2.12.9
	rivalA, rivalB, diff = bitter_rivals(vd)
	ans = '{} and {} are the most disimilar senators with an index of {}'
	print(ans.format(rivalA, rivalB, diff))
	