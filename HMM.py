"""Hidden Markov Model Toolkit

"""

""" 
From the AAAI Workshop on Model AI assignments.
"""


import random
import argparse
import codecs
import os

# observations
class Observation:
    def __init__(self, stateseq, outputseq):
        self.stateseq  = stateseq   # sequence of states
        self.outputseq = outputseq  # sequence of outputs
    def __str__(self):
        return ' '.join(self.stateseq)+'\n'+' '.join(self.outputseq)+'\n'
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.outputseq)

# hmm model
class HMM:
    def __init__(self, transitions=None, emissions=None):
        """creates a model from transition and emission probabilities"""
        self.transitions = transitions
        self.emissions = emissions
        if self.emissions:
            self.states = self.emissions.keys()

    ## part 1 - you do this.
    def load(self, basename):
        """reads HMM structure from transition (basename.trans),
        and emission (basename.emit) files,
        as well as the probabilities if given.
        Initializes probabilities randomly if unspecified."""

        pass

   ## part 1 - you do this.
    def dump(self, basename):
        """store HMM model parameters in basename.trans and basename.emit"""

        pass
   ## part 2 - you do this.
    def generate(self, n):
        """return an n-length observation by randomly sampling from this HMM.
        """

        pass

    ## do this for pt 4.
    def viterbi(self, observation):
        """given an observation,
        set its state sequence to be the most likely state sequence that generated
        the output sequence, using the Viterbi algorithm.
        """

        pass

      # part 3: you do this.
    def forward(self, observation):
        """given an observation as a list of T symbols,
        compute and return the forward algorithm parameters alpha_i(t)
        for all 0<=t<T and i HMM states.
        """

        pass
        ## helper for part 3
    def forward_probability(self, observation):
        """return probability of observation, computed with forward algorithm.
        """
        # TODO: fill in for section e
        pass


