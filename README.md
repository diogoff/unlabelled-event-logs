# Discovering Process Models from Unlabelled Event Logs

This repository contains the source code for the paper [Discovering Process Models from Unlabelled Event Logs](http://web.tecnico.ulisboa.pt/diogo.ferreira/papers/ferreira09discovering.pdf) presented at the _7th International Conference on Business Process Management_ (BPM 2009) in Ulm, Germany, September 7-10, 2009.

### Files

The approach is referred to as the _Multiple Instance Model_ (MIM) and the source code comprises three main files:

- `mim.py` contains the Python class `model` and the routines to estimate the model parameters, namely the transition matrix **M**, the global transition matrix **M<sup>+</sup>** used to initialize **M**, the source sequence **s**, and the separated source sequences **y<sup>(1…K)</sup>** that can be obtained from the symbol sequence **x** and the source sequence **s**.

- `mimest.py` contains the sample code for creating and estimating a multiple instance model from a symbol sequence **x**. The input sequence is read from standard input with one symbol per line.

- `mimgen.py` contains useful code to generate a symbol sequence **x** from a distribution of sequences with different probabilities, using a number of instances and a number of overlapping instances as specified in the input parameters.

In general, only `mim.py` and `mimest.py` will be required. Basically, `mimest.py` imports and invokes `mim.py` in order to estimate a model. To test this code one must have a sample symbol sequence **x** and therefore `mimgen.py` is provided as a utility program to generate such sample sequence. For this purpose, an additional example file is provided:

- `example.txt` contains a sample distribution to be used as input to `mimgen.py` in order to create a symbol sequence **x** that can given to mimest.py.

### Instructions

Here is a tutorial example on how to use the code:

1. Start by looking at the contents of `example.txt`, which basically contains the behavior that will be used to create the output symbol sequence **x**. In each line there is a sequence and its corresponding probability. These probabilities should add up to 1.0, but the code in `mimgen.py` will normalize the distribution even if this is not the case.

2. Assuming that Python 2 is installed and available in the system, open a command line and run:
   ```
   $ python mimgen.py 20 5 example.txt sequence.txt
   ```
   In this example, were are asking for a symbol sequence to be generated from a set of 20 instances (i.e. 20 sequences drawn from the set of possible sequences found in `example.txt`) and using a maximum number of 5 overlapping instances (i.e. at any moment there will be no more than 5 active instances). The input sequence distribution is to be read from `example.txt` and the output symbol sequence **x** is to be written to `sequence.txt`.

3. Check the output that `mimgen.py` produces on the screen. In this example, the results could look like something similar to the following picture. Note that the actual results may differ since `mimgen.py` is picking the sequences and interleaving them randomly.




### Reference

See the [publisher's website](https://link.springer.com/chapter/10.1007%2F978-3-642-03848-8_11).
