# -*- coding: utf-8 -*-
"""Euler 14 15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2k1c-17_C1-hlr59mQx7TpZr0iDPQTA
"""

import numpy as np
import pandas as pd
import string
import math
from itertools import permutations, combinations
import time

"""#14 Longest Collatz Sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)

n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def make_collatz_sequence(starting_number):
  current_number = starting_number
  sequence = []

  sequence.append(current_number)

  while current_number > 1:
    if current_number % 2 == 0:
      next_number = int(current_number / 2)
      sequence.append(next_number)
    else:
      next_number = int(3 * current_number + 1)
      sequence.append(next_number)
    
    current_number = next_number
  
  return sequence

make_collatz_sequence(13)

lengths = []
i = 1

while i < 1000000:
  current_sequence = make_collatz_sequence(i)

  length_of_sequence = len(current_sequence)
  lengths.append([i, length_of_sequence])

  i += 1

as_dataframe = pd.DataFrame(lengths)

sorted = as_dataframe.sort_values(by=[1])

sorted.tail()

"""#15 Lattice Paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

![euler_15.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANAAAACXAQMAAABeN0fjAAAABlBMVEVsAGUAAADWqXHfAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+MDCREdAmoqMqEAAAAkdEVYdENvbW1lbnQAVWxlYWQgR0lGIFNtYXJ0U2F2ZXIgVmVyIDIuMLqaStoAAAGnSURBVEjH7dexboMwEAbgQ45Eh6p0zBT3QSrxWtlg6INZyot4yAN49GDhGuy7BptzKrVqpIpbkvBhMOJs/QHAarz34/JNem/nz97P5SIpJFdQHCjToUgTjRpx1KFGbwCvAKdAACJS+P2+006/QbFFv0GhRU2k28bGFu1i98ZRehnVzxro6faCenUvojC95pHUhdlHmqe4opZoKMkRqTUJor4kSzSuqSGSJRmi/LmIupI00pTTgNSWpJDcXToS9WMiYSOdeJIjkqSXYhJpnizSCxKkVyknnvxHomcihS16LXZs9bVjb1dXJctQuKjmaWRpApYsT5on9lbz+uDqCHv9o4qdHvqnpc18SD0fl1pYLC2uWTgvhw477fR3tGpRdY+GJZ0gTbeNfU479orogk95PBAPphRFtqitkeNI1Mhy1NTIsM9VI83SUCF1jy5EeRQRF4V0Ksgg5VFEXByRzskTZVEkkEKaCjJIWRQJkdjR3nvd+vM4bEWROgGSzckBZpssH4h59WxHEUHnzsEzIzxX5oFIUGyRJieallQ5GTalCMWmFPHzlPIJSygqFqlA3XYAAAAASUVORK5CYII=)

If a 2x2 grid means four little path segments, a 20x20 grid means 40 little path segments.  Twenty must be "down" and twenty must be "right."  This is identical to how many orders you can pick 20 red and 20 blue marbles out of a bag.
"""

# 40! / 20! * 20!

denominator = math.factorial(20) * math.factorial(20)
numerator = math.factorial(40)

numerator / denominator