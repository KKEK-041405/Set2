Python has several functions for creating, reading, updating, and deleting file

s

The open() function takes two parameters; filename, and mode

.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

PROGRAM:

filename=input('Enter a file name')

f=open(filename,'r')

alphabet_buckets={}

for word in f.read().split():

 if(word[0].isalpha()):

 temp=word.lower()

 if(temp[0] not in alphabet_buckets.keys()):

 alphabet_buc

kets[temp[0]]=[]

 alphabet_buckets[temp[0]].append(temp)

 else:

 alphabet_buckets[temp[0]].append(temp)

print(alphabet_buckets)

f.close()

