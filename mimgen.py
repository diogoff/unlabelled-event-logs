import sys
import mim
import math
import random

# prints the sequences in a similar way to fig.2 in the paper
def printseqs():
	T = len(str(ninstances))
	N = len(str(len(symbolseq)))

	# print sequence positions
	for i in reversed(range(1,N+1)):
		factor = int(math.pow(10,i-1))
		last_digit = 0
		line = (T+1)*' '
		for j in range(0,len(sourceseq)):
			digit = ((j+1)/factor) % 10
			if i == 1:
				line += str(digit)
			else:
				if digit != last_digit:
					line += str(digit)
				else:
					line += ' '
			last_digit = digit
		print line

	# print symbol sequence
	line = (T+1)*' '
	for symbol in symbolseq:
		line += str(symbol)
	print line

	# print sequences for each instance
	for i in range(0,ninstances):
		source = i + 1
		line = (T-len(str(source)))*' '
		line += str(source)
		line += ' '
		for j in range(0,len(sourceseq)):
			if sourceseq[j] == source:
				line += symbolseq[j]
			else:
				line += '.'
		print line
		
	# print symbol sequence
	line = (T+1)*' '
	for symbol in symbolseq:
		line += str(symbol)
	print line

	# print source for each event
	for i in reversed(range(1,T+1)):
		factor = int(math.pow(10,i-1))
		line = (T+1)*' '
		for j in range(0,len(sourceseq)):
			digit = (sourceseq[j]/factor) % 10
			if i == 1:
				line += str(digit)
			else:
				if digit > 0:
					line += str(digit)
				else:
					line += ' '
		print line

	# get the number of simultaneously active sources at each position
	simultaneous = []
	max_count = 0
	for i in range(0,len(sourceseq)):
		left = []
		right = []
		for j in range(0,i+1):
			if sourceseq[j] not in left:
				left.append(sourceseq[j])
		for j in range(i,len(sourceseq)):
			if sourceseq[j] not in right:
				right.append(sourceseq[j])
		count = 0;
		for source in left:
			if source in right:
				count += 1
		simultaneous.append(count)
		if count > max_count:
			max_count = count

	# print the number of active sources at each position
	for i in reversed(range(1,len(str(max_count))+1)):
		factor = int(math.pow(10,i-1))
		line = (T+1)*' '
		for count in simultaneous:
			digit = (count/factor) % 10
			if i == 1:
				line += str(digit)
			else:
				if digit > 0:
					line += str(digit)
				else:
					line += ' '
		print line

# main routine begins here

if len(sys.argv) < 5:
	print 'Missing overlap value.'
	print 'Usage: {0} <no.instances> <overlap> <input-file> <output-file>'.format(sys.argv[0])
	print '  \'no.instances\' specifies the number of instances to be created'
	print '  \'overlap\' specifies the number of overlapping instances'
	print '  \'input-file\' is the input file containing the sequences and their weigths'
	print '  \'output-file\' is the output file where the symbol sequence will be written'
	exit()

# read one sequence per line, together with a probability value

fin = open(sys.argv[3], 'r')

seqprobs = dict()

for line in fin:
	[z, p] = line.split()
	if len(z) > 0:
		seqprobs[z] = float(p)

fin.close()

mim.normalize(seqprobs)

# select instances to be used

ninstances = int(sys.argv[1])
if ninstances < 1:
	ninstances = 1;
	print 'using default no. instances = {0}'.format(ninstances)

overlap = int(sys.argv[2])
if overlap < 1:
	overlap = 1;
	print 'using default overlap = {0}'.format(overlap)

random.seed()

sequences = dict()

for k in range(0,ninstances):
	psum = 0.0
	p = random.random()
	for z in seqprobs.iterkeys():
		psum += seqprobs[z]
		if p < psum:
			sequences[k+1] = z[:]
			break

# generate symbol sequence

symbolseq = []
sourceseq = []

upperbound = 0

while len(sequences) > 0:
	sources = sequences.keys()
	selected = random.randint(0,min(overlap-1,len(sources)-1,upperbound))
	if selected >= upperbound:
		upperbound += 1
	source = sources[selected]
	symbol = sequences[source][0]
	symbolseq.append(symbol)
	sourceseq.append(source)
	if len(sequences[source]) <= 1:
		del sequences[source]
		upperbound -= 1
	else:
		sequences[source] = sequences[source][1:]
	
# print sequences

printseqs()

# write symbol sequence to output file

fout = open(sys.argv[4], 'w')

for xn in symbolseq:
	fout.write(xn)
	fout.write("\n")

fout.close()

# main routine ends here
