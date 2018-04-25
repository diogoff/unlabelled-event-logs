import sys
import mim

# read symbol sequence x from stdin, with one symbol per line
x = []
for line in sys.stdin:
	symbol = line.strip()
	if len(symbol) > 0:
		x += [symbol]

# print the sequence as string
print "Symbol sequence: ", mim.seq2str(x)

print "({0} symbols)".format(len(x))

# create to be estimated from sequence x
m = mim.model(x)

# estimate model
K = m.estimate()

# print model
m.printmodel(m.M)

# show the probability distribution of the different sequences in the model
pz = mim.sortbyvalue(m.seqprobs())
for z, p in pz:
	print '{0:.3f} : {1}'.format(p, z)

print 'Total number of sources: {0}'.format(K)
