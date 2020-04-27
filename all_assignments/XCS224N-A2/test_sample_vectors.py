import os
from utils.sanity_checks import sample_vectors_expected
from utils.utils import load
import numpy as np
from pprint import pprint

# tester code for checking the output vectors generated by run.py.
sampleVectorsPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sampleVectors.json")
if not os.path.isfile(sampleVectorsPath):
    raise Exception('Excecute run.py file before excecuting this file')

sample_vectors_actual = load(sampleVectorsPath)

test_words = ["female", "cool"]

for word in test_words:
    print("Your output")
    pprint(sample_vectors_actual[word])
    print("\nExpected output")
    pprint(sample_vectors_expected[word])
    print("\nAre the vectors similar: ",
          np.allclose(sample_vectors_actual[word], sample_vectors_expected[word], rtol=1e-3))

    print("\n"*3)
