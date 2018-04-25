# Discovering Process Models from Unlabelled Event Logs

This repository contains the source code for the paper entitled _Discovering Process Models from Unlabelled Event Logs_ presented at the _7th International Conference on Business Process Management_ (BPM 2009) in Ulm, Germany, September 7-10, 2009.

The approach is referred to as the _Multiple Instance Model_ (MIM) and the source code comprises three main files:

- `mim.py` contains the Python class model and the routines to estimate the model parameters, namely the transition matrix **M**, the global transition matrix **M<sup>+</sup>** used to initialize **M**, the source sequence **s**, and the separated source sequences **y<sup>(1…K)</sup>** that can be obtained from the symbol sequence **x** and the source sequence **s**.

- `mimest.py` contains the sample code for creating and estimating a multiple instance model from a symbol sequence **x**. The input sequence is read from standard input with one symbol per line.

- `mimgen.py` contains useful code to generate a symbol sequence **x** from a distribution of sequences with different probabilities, using a number of instances and a number of overlapping instances as specified in the input parameters.

In general, only `mim.py` and `mimest.py` will be required. Basically, `mimest.py` imports and invokes `mim.py` in order to estimate a model. To test this code one must have a sample symbol sequence **x** and therefore `mimgen.py` is provided as a utility program to generate such sample sequence. For this purpose, an additional example file is provided:

- `example.txt` contains a sample distribution to be used as input to `mimgen.py` in order to create a symbol sequence **x** that can given to mimest.py.

