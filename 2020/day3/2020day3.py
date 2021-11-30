import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2020day3input.txt")) as f:
    dataset = f.read().split('\n')