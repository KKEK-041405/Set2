DESCRIPTIO

N

:

Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and

ArrayList in Java). In simple language, a list is a collection of t

hings, enclosed in [ ] and separated

by commas.

PROGRAM:

names = ['Arun', 'Varun', 'Kent', 'Eat', 'Pot', 'net', 'Peak', 'Peacock', 'Zebra', 'Nato', 'Toe', 'Poke',

'Knife

', 'Peot', 'Venus', 'Ant']

letters = ['A', 'K', 'E', 'O','T', 'P', 'N']

for name in na

mes:

 cnt=0
  uni = list(set(name.upper()))

 for letter in uni:

 if letter in letters:

 cnt+=1

 if cnt==len(name):

 print(name)
