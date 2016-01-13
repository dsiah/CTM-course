from functools import reduce

def dict2List(dct, keylist): return [dct[i] for i in keylist]

def list2Dict(L, keylist): return {i:j for (i, j) in zip(keylist, L)}

def listrange2Dict(L): return {i:j for (i, j) in zip(range(len(L)), L)}

def makeInverseIndex(strlist):
	idict = {} 
	
	for i, line in enumerate(strlist):
		words = line.split() # each line is a 'document' consisting of words
		
		for word in words:
			# add line (document number to word's set)
			idict[word] = idict.get(word, set()) # if it doesn't exist create a set
			idict[word].add(i)

	return idict

def orSearch(inverseIndex, query):
	# Return set of document numbers containing -any- of the words in the query
	sets = [inverseIndex[word] for word in query] # List of sets that contain word
	return reduce(lambda a, b: a | b, sets) 

def andSearch(inverseIndex, query):
	# Return set of document numbers containing -all- of the words in the query
	sets = [inverseIndex[word] for word in query] # List of sets that contain word
	return reduce(lambda a, b: a & b, sets)


if __name__ == '__main__':
	f = list(open('stories_big.txt'))

	inv_ind   = makeInverseIndex(f)  #inverse index
	or_trial  = orSearch(inv_ind, ['cubic', 'the'])
	and_trial = andSearch(inv_ind, ['cubic', 'the'])

	print(or_trial)
	print(orSearch(inv_ind, ['cubic']))
	print(and_trial)