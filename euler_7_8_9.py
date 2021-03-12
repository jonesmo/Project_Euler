# -*- coding: utf-8 -*-
"""Euler 7 8 9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HKrtAwBMOACQHZibDyfEWkkW3YAZUVjv
"""

import numpy as np
import pandas as pd
import string
import math
from itertools import permutations, combinations

"""###7 10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def find_primes(number):
  for j in range(2, int(np.rint(number * 0.5))):
    if number % j == 0:
      return False
  else:
    return True

primes_list = []
i = 2

while len(primes_list) <= 10001:
  i_bool = find_primes(i)
  if i_bool == True:
    primes_list.append(i)
  i += 1

len(primes_list)

primes_list[::-1][0]

"""###8 Largest Product in a Series
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

thousand_digit = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

#I'll find the 13 adjacent digits with the largest sum and then multiply them together
#I have to watch for zeroes

digit_version = [int(x) for x in str(thousand_digit)]

i = -1
products = []

while i <= (1000-13):
  i += 1
  endpoint = i + 13
  chunk = digit_version[i:endpoint]
  if 0 in chunk:
    #print('Skipping, zero present')
    continue
  else:
    product_of_chunk = np.prod(chunk)
    products.append(product_of_chunk)

products[0:10]

len(products)

sorted = np.sort(products)

sorted[::-1][0]

"""###9 Special Pythagorean Triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*So we're looking for three different integers whose sum is 1000 and who fulfill the Pythagorean theorem.*

*Should I start by making a list of all the triples that sum to 1000?  That's a lot of triples.  Might be better to start with finding all the Pythagorean triples. Does that mean I have to make a list of all possible permutations of three integers below 1000 and then testing to see if they fulfill the Pythagorean theorem?  I suspect there's a more efficient way.*
"""

pythagorean_triples = []

for integer in range(1,998):
  a = integer
  for integer2 in range(1, 998):
    b = integer2
    for integer3 in range(1, 998):
      c = integer3
      if (a == b) or (b == c) or (a == c):
        continue
      if a + b + c == 1000:
        if (a**2 + b**2 == c**2):
          pythagorean_triples.append([a, b, c])

pythagorean_triples

#okay that was not a good way, let's try again but checking for Pythagorean triple first

pythagorean_triples = []

def find_pythagorean_triple(x, y, z):
  if x**2 + y**2 == z**2:
    return True
  else:
    return False

find_pythagorean_triple(5, 12, 13)

#now find a list of sets of three different integers that sum to 1000
possibles = list(range(1,1000))
possibles

three_integer_sets = combinations(possibles, 3)

pythagoreans = []

for set_of_three in three_integer_sets:
  a = set_of_three[0]
  b = set_of_three[1]
  c = set_of_three[2]
  is_pythagorean = find_pythagorean_triple(a, b, c)
  if is_pythagorean is True:
    pythagoreans.append(set_of_three)

pythagoreans

for pythagorean_triple in pythagoreans:
  a = pythagorean_triple[0]
  b = pythagorean_triple[1]
  c = pythagorean_triple[2]
  if (a + b + c != 1000):
    continue
  else:
    answer = pythagorean_triple
    print(answer)

product = answer[0] * answer[1] * answer[2]

product