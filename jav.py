#CONSTANTS
#Fixed values such as numbers, letters, and strings, are called "constants" because their value does not change.
#Numeric constant are as you expect
#String constants use single quotes (') or doble quotes ("")
#print (123)
#print ('Hola amigos')
#DONT USE RESERVED WORDS
#A variable is a named place in the memory where a programmer can store data and later retrieve the date using the variable "name"
#Programmers get to choose the names of the variables
#You can change the contents of a variable in a later statement
#x = 12.2
#y = 14
#we can change the variables
#don't start with a number or _

#from turtle import clear


#a = 35
#b = 12.50
#c = a*b
#print(c)

#EXPRESSIONS...

#We have operators, that are very much same as the mathematical operators:
# +  --- Addition
# - --- Substraction
# * --- Multiplication
# / --- Division
# ** --- Power
# % --- Remainder

#Remainder is pretty tricky xd\
#jj = 23
# kk = jj % 5
# print(kk)
#es lo que sobra de de una division

 #OPERATOR PROCEDENCE
 #x=1 + 2 * 3 - 4 / 5 ** 6
 #x=1 + (2 * 3) - (4 / (5 ** 6))
 
 #OPERATOR PROCEDENCE RULES
 #Parenthesis > Power > Divison > Multiplication > Addition > Left to Right
 
#CONCATENATE
#eee = 'hello' + 'there'
#print(eee)
#hello there


# we can't opperate letters with numbers!!!!

#we can ask Python what type something is by using the type() function
#str, integers, float


#Integer division produces a floating point result
#print(10 / 2)
#5.0

#INPUT
#nam = input ( 'who are you?' )
#print('welcome',nam)

#CONDITIONAL EXECUTION
#the beginning of male python make desitions for US
#if is the reserved word
#CODE
#x = 5
#if x < 10:
 #print( 'smaller' )
#if x > 20:
    #print( 'bigger' )
#The question is always followed by the answer with a space
#print( 'finis' )
#FLUX DIAGRAM FOR IF AND CONDITIONALS
#COMPARISON OPERATORS
#< less than
#<= less than or equal to
#== equal to
#>= greater than or equal to
#> greater than 
#!= not equal
#IMPORTANT MAKE BLOCS!
#IDENTATION
#---Increase indent indent after an if statement or for statement (after:)
#---Maintain indent to indicate the scope of the block (which lines are affected by the if/for)
#---Reduce indent back to the level of the if statement or for statemente to indicate the end of the block
#---Black lines are ignored - they do not affcet identation
#---Comments on a line by themselves are ignored with regard to identation

#MORE CONDITIONAL STRUCTURES

#x = 5
#if x < 2 :
 #   print ('small')
#elif x > 10 :
#    print ('Medium')
#else :
#        print('Ginormous')

#THE TRY / EXCEPT STRUCTURE
#you surround a dangerous section of code with try and except
#If the code in the try works / the except is skipped
#if the code in the try fails / it jumps to the except

#the try is only triggered at te function if it blows up, if it doesnt it will triggered to the except


#astr= 'Hello bob'
#try:
 #str = int (astr)
#except: istr = -1
#print('first', istr)



#-----------------------------------------------------------------------------
#FUNCTIONS
#def is to store functions

#DEFINITION OF THE FUNCTION
#def thing():
 #print('hello')
 #print('Fun')

#INVOCATION OF THE FUNCTION
#thing()
#print('zip')
#thing()

#we colocate def before a function, like input() type() float() int () print ()

#max and min funciton chosees the letter that is more at the end in the alphabet


#tiny = max('Hello zeeeglr')
#print(tiny)

#we use the def keyword followed by optioinal parameters in parentheses 
#we indent the body of the function
#this defines the function but does not execute the body of the function

#the things inside the identention isnt executed
#once whe have defined a function, we can call (or invoke) it as many times as we like
#this is the store and reuse pattern

#EXAMPLE----
#def print_lyrics() :
 #print("Im a ...")
 #print("Im a XDD...")

#print_lyrics()      ----- invoke

#ARGUMENTS
#An argument is a value we pass into the function as its input when we call the function
#We use arguments si we cab durect the function to do different kinds of work  when we call it a t different times
#We put the arguments in parentheses after the name of the function

#PARAMETERS
#A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the code in the function to access the arguments for a particular function invocation.


#def greet(lang)
 #if lang == "es":
  #print('hola')
#elif lang == 'fr':
 #print('bonjour'
#else:
 #print('hello')

#RETURN VALUES
#Often a function will take its arguments, do some compulation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.



#LOOPS AND ITEARION
#n=5
#while n > 0:
 #print(n)
 #n=n-1
#print('blastoff!')
#print(n)

#Loops (repeated steps) have iteration variables that change each time through a loop. Oten these iteartion variables go through a sequence of numbers.


#BREAKING OUT OF A LOOP
#The break statement ends the current loop and jumps to the statemen inmediately following the loop
#It is like a loop test that can happen anywhere in the body of the loop

#while True:
 #line = input('> ')
 #if line == 'done' :
  #break
 #printe(line)
#print('Done!')



#CONTINUE IS ANOTHER LOOP STATEMENT LIKE BREAK
#It is like go up back to the top of the loop

#While true:
 #line = input('> ')
 #if line[0] == '#':
   #continue
 #if line == 'done': 
   #break
 #print(line)
#print(done!)

#n = 0
#while True:
  #  if n == 3:
#        break
 #   print(n)
 #   n = n + 1

#LOOP IDIOMS

#the trick is "knowing" something about the whole loop when you are stuck writing code 
#that only sees one entry at time

#print('before')
#for thing in [9, 41, 12, 3, 74, 15] :
#   print (thing)
#print('after')


#largest_sofar = -1
#print('before', largest_sofar)
#for the_num in[9,41,12,3,74,15] : 
#  if the_num > largest_sofar :
#    largest_sofar = the_num
#  print(largest_sofar, the_num)
#print('after', largest_sofar)

#COUNTING IN A LOOP
#the count how many times we execute a loop, we introduce a counter vaiable
#that starts at 0 and we add one to it each ti,e through the loop.

#zork = 0
#print('before', zork)
#for thing in [9, 41, 12, 3, 74, 15] :
#  zork = zork + 1
#  print(zork, thing)
#print('after', zork)

#We can also sum the total
#zork = 0
#print('before', zork)
#for thing in [9, 41, 12, 3, 74, 15] :
#  zork = zork + thing
#  print(zork, thing)
#print('after', zork)


#THE AVERAGE
#count = 0
#sum = 0
#print('before', count, sum)
#for value in [9, 41, 12, 3, 74, 15] :
#  count = count + 1
#  sum = sum + value
#  print (count, sum, value)
#print('after', count, sum, sum / count)

#LOOKING OR HUNTING FOR THINGS
#print('before')
#for value in [9, 41, 12, 3, 74, 15]:
#  if value > 20 :
#    print('the number is larger than 20, and is: ', value)
#print ('after')

#SEARCH USING A BOOLEAN VARIABLE
#found = False
#print('before', found)
#for value in [9, 41, 12, 3, 74, 15] :
#  if value == 3 : 
#    found = True
#  print(found, value)
#print('after', found)

#FINDING THE SMALLEST VALUE
#smallest = None
#print('before')
#for value in [9, 41, 12, 3, 74, 15] : 
#  if smallest is None : 
#    smallest = value
#  elif value < smallest : 
#    smallest = value
#  print (smallest, value)
#print('after', smallest)

#we can use None to indicate emptiness, nothing. A very useful variable

#IS AND IS NOT OPERATORS
#Python has an is operator that can be used in logical expressions
#implies ' is the same as '
#similar to, but stronger than ==
#is not also is a logical operator
#is stronger because should be equal the type and the value of the variable
#use it in booleans and none 



#-----------------------------------------------------------------------------------------
#STRINGS
#a string is a sequence of characters
#a string literal uses quotes 'Hello' or "Hello"
#For strings, + means'concatenate'
# when a string contains numbers, it is still a string
# we can convert numbers in a string into number using int() 
#we prefer to raead data in using strings and the parse and convert the data as we need
#this give us more control over error situations and/or bad user input
#raw input numbers must be converted from strings

#we can get at any single character in a string using an index specified in square blanckets
#the index value must be an integer and starts at zero
#the index value can be an expression that is computed


#fruit = 'banana'
#letter = fruit[1]
#print(letter)

#x = 3
#w = fruit [x - 1]
#print(w)

#you will get a python error if you attempt to index beyond the end of a string
#so be careful when constructing index values and slices

#len FUNCTION
#give us the lenght of the word characters in the string
#fruit = 'banana'
#x = len (fruit)
#print(x)

#LOOPING THROUGH STRINGS
#Using a while statement and an iteration variable, and the len fuction, we can construct
# a loop to look at each of the letters in a string individually

#fruit = 'banana'
#index = 0
#while index < len(fruit) : 
#  letter = fruit[index]
#  print(index, letter)
#  index = index + 1

#a definite loop using a for statement is much more elegant
#the iteration variable is completely taken care of by the for loop

#fruit = 'banana'
#for letter in fruit :
#  print(letter)

#index = 0
#while index < len(fruit) : 
#  letter = fruit[index]
#  print(letter)
#  index = index + 1

#LOOPING AND COUTING
#this is simple llop that loops through each letter in a string and counts 
#the number of times the loop encounters the 'a' character

#ord = 'banana'
#count = 0
#for letter in word :
#  if letter == 'a' :
#    count = count + 1
#print(count)
#this code counts the as in the word banana

#LOOKING DEEPER INTO IN
#The iteration variable 'iterates' through the sequence (ordered set)
#the block (body) of code is executed once for each value in the sequence

#for letter in 'banana':
#  print(letter)

#SLICING STRINGS

#we can also look at any continuos section of a string using a color operator
#the second number is one beyond the end of the slice 'up to but not incluiding'
#if the second number is beyond the end of the string, it stops at the end.

#s = 'Monty Python'
#print(s[0:4])
#print(s[6:7])
#print(s[6:20])

#STRING CONCATENATION
#When the + operator is applied to strings, it means 'concatenation'

#a = 'hello'
#b = a + 'there'
#print(b)

#c = a + ' ' + 'there'
#print(c)

#Using in as a logical operator
#the in keyword can also be used to check to see if one string is 'in' another string
#the in expression is a logical expression that returns true or false and can be used in an 
#if statement

#fruit = 'banana'
#'n' in fruit 

#'m' in fruit

#'nan' in fruit

#if 'a' in fruit : 
 # print('found it!')


#STRING LIBRARY 
#python has a number of string functions which are in the string library

#these functions are already built into every string -we invoke them by appending 
#the function to the string variable

#these functions do not modify the original string , instead they return a new string that
#has been altered


#greet = 'HElLo Bob'
#zap = greet.lower()
#print(zap)

#print('Hi There'.lower())

#stuff = 'Hello Word'
#print(stuff.upper())

#SEARCHING A STRING
#We use the find() function to search for a substring within another string
#find() finds the first occurrence of the substring
#if the substring is not found, find() returns -1
#remember that string position starts at zero

#fruit = 'banana'
#pos = fruit.find('na')
#print(pos)

#aa = fruit.find('z')
#print(aa)

#MAKING EVERYITHING UPPER CASE
#you can make a copy of a string in lower case or upper case.
#often when we are searching for a string using find() we first convert the string to lower
#case so we can search a string regardless of case.

#greet = 'Hello Bob'
#nnn = greet.upper()
#print(nnn)

#www = greet.lower()
#print(www)

#SEARCH AND REPLACE
#The replace() function is like a 'search and replace' operation in a word processor
#It replaces all occurrences of the search string with the replacement string

#greet = 'Hello Bob'
#nstr = greet.replace('Bob', 'Jane')
#print (nstr)

#nstr = greet.replace('o', 'X')
#print (nstr)

#STRIPPING WHITESPACE
#sometimes we want to take a string and remove whitespace at the beginning and/or end
#Istrip() and rstrip() remove whitespace at the left or right
#strip() removes both beginning and ending whitespace

#greet =  '       Hello Bob '
#print (greet.lstrip())
#print (greet.rstrip())
#print (greet.strip())

#PREFIXES
#line = 'Please have a nice day'
#line.startswith('Please')

#line.startswith('p')


#PARSING AND EXTRACTING
#data = 'From jav.@gmail.com Sat Jan 5 09:14:16 2009'
#atpos = data.find('@')
#print(atpos)

#sppos = data.find(' ', atpos)
#print(sppos)

#host = data[atpos+1 : sppos]
#print(host)



#Reading FILES
#FILE PROCESSING
#A text file can be thought of as a sequence of lines
#OPENING A FILE
#Before we can read a the contents of the file, we must tell Python which file we are going
#to work with and what we will be doing with the file
#This is done with the open() function
#open() returns a "file handle" - a variable used to perform operations on the file
#Similar to "File -> Open" in a Word Processor

#USING open()
#handle = open(filename, mode)
#returns a handle use to manipulate the file
#filename is a string
#mode is optional and should be 'r' if we are planning to read the file and 'w' if we are
#going to write the file

#THE NEWLINE CHARACTER
#We use a special characer called the "newline" to indicate when a line ends
#we represent it as \n in strings
#Newline is still one character, no two

#stuff = 'Hello \nworld!'
#print(stuff)

#FILE HANDLE AS A SEQUENCE
#A file handle open for read can be treated as a sequence of strings where each line in the file
#is a string in the sequence
#We can use the for statement to iterate through a sequence 
#remember -a sequence is an ordered set

#xfile = open('mbox.txt')
#for cheese in xfile : 
#  print(cheese)

#Open a file read-only
#Use a for loop to read each line
#Count the lines and print out the number of lines

#fhand = open ('mbox.txt')
#count = 0
#for line in fhand : 
#  count = count + 1
#print ('Line Count:', count)

#Reading the 'Whole' File
#We can read the whole file (newlines and all) into a single string

#fhand = open ('mbox.txt')
#inp = fhand.read()
#print (len(inp))

#print(inp[:20])
#printing the first 20 characters

#SEARCHING THROUGH A FILE
#We can put an if statement in our for loop to only print lines that meet some criteria
#fhand = open('mbox.txt')
#for line in fhand : 
#  if line.startswith('From:') :
#    print(line)

#Each line from the file has a newline at the end
#the print statement adds a newline to each line

#we can strip the whitespace from the right-hand side of the string using rstrip() from 
#the string library
#the newline is considered 'white space' and is stripped

#fhand = open ('mbox.txt')
#for line in fhand : 
#  line = line.rstrip()
#  if line.startswith('From:') :
#    print (line)

#SKIPPING WITH CONTINUE
#We can conveniently skip a line by using the continue statement

#fhand = open ('mbox.txt')
#for line in fhand :
#  line = line.rstrip()
#  if not line.startswith('From:') :
#    continue
#  print(line)

#fhand = open('mbox.txt')
#for line in fhand :
#  line = line.rstrip()
#  if not 'XD:' in line :
#    continue
#  print(line)

#fname = input('Enter the file name: ')
#try:

#  fhand = open(fname)
#except:
#  print('File cannot be opened: ', fname)
#  quit()
#count = 0
#for line in fhand :
#  if line.startswith('From:') : 
#    count = count + 1
#print('There were', count, 'subject lines in', fname)

#Programming
#ALGORITMS
#A set of rules or steps used to solve a problem
#DATA STRUCTURES
#A particular way of organizing data in computer

#What is not a 'Collection'
#Most of our variables have one value in them -when we put a new value in the variable
#the old value is overwritten


#A list is a kind of Collection
#A collection allows us to put many values in a single 'variable'
#A collection is nice because we can carry all many values around in on e convenient package

#friends = [ 'Joseph', 'Gleen', 'Sally' ]
#carryon = [ 'socks', 'shirt', 'perfume' ]

#LIST CONSTANTS
#List constants are sorrounded by square brackets and the elements in the list are separated
#by commas
#A list element can be any Python object -even another list
#A list can be empty


#for i in [5,4,3,2,1] :
#  print (i)
#print('the end')

#friends = ['Joseph', 'Glenn', 'Sally']
#for friend in friends :
#  print ('Happy New Year: ', friend)
#print ('Done!')

#LOOKING INSIDE LISTS
#Just like strings, we can get at any single element in a list using an index specified in 
#square brackets


#friends = ['Joseph', 'Glenn', 'Sally']
#print(friends[1])

#LIST ARE MUTABLE
#Strings are 'mutable' - we cannot change the contetns of a string - we must make a new string
#List are 'mutable' -we can change any element of a list using the index operator

#fruit = 'Banana'
#x = fruit.lower()
#print(x)

#lotto = [2, 14, 26, 41, 63]
#lotto[2] = 28
#print(lotto)

#fruit = 'banana'
#x = fruit[1]
#print(x)

 #HOW LONG IS A LIST?
 #The len() function takes a list as a paremeter and returns the number of elements in the list
 #Actually len() tells us the number of elements of any set or sequence (such a string...)

#greet = 'Hello Bob'
#print(len(greet))

#x = [1, 2, 'joe', 99]
#print(len(x))

#USING THE RANGE FUNCTION
#The range function returns a list of numbers that range from zero to one less than the parameter
#We can construct an index loop using for and an intefer iterator

#print(range(4))

#friends = ['Joseph', 'Glenn', 'Sally']
#print(len(friends))
#print(range(len(friends)))

#for friend in friends :
#  print('Happy New Year: ', friend)

#for i in range(len(friends)) : 
#  friend = friends [i]
#  print('Happy New Year :', friend)


#CONCATENATING LISTS USING +
#We can create a new list by adding two existing lists together

#a = [1,2,3]
#b = [4,5,6]
#c = a + b
#print(c)
#print(a)
#print(b)

#LIST CAN BE SLICED USING:
#t = [9,41,12,3,74,15]
#print(t[1:3])

#print(t[:4])

#LIST METHODS
#x = list ()
#print(type(x))
#print(dir(x))

#We can create an empty list and then add elements using the append method
#The list stays in order and new elements are added at the end of the list

#stuff = list()
#stuff.append('book')
#stuff.append(99)
#print(stuff)

#stuff.append('coockie')
#print(stuff)

#IS SOMETHING IN A LIST?
#Python provides two operators that let you check if an item is in a list
#These are logical operators that return True or False
#They do not modify the list

#some = [1,9,21,10,16]
#print(9 in some)
#print(15 in some)
#print (20 not in some)


#LIST ARE IN ORDER
#A list can hold many items and keeps those items in the order until we do something to change
#the order
#A list can be sorted (i.e., change its order)
#The sort method (unlike in strings) means 'sort yourself'

#friends = ['Joseph','Glenn', 'Sally']
#friends.sort()
#print(friends)
#print(friends[1])

#BUILT-IN FUNCTIONS AND LISTS
#There are a number of functions built into Python that take lists as parameters
#Remember the loops we built? these are much simpler

#nums = [3,41,12,9,74,15]
#print(len(nums))
#print(max(nums))
#print(min(nums))
#print(sum(nums))
#print(sum(nums)/len(nums))

#numlist = list()
#while True :
#  inp = input('Enter a number: ')
#  if inp == 'done' : break
#  value = float(inp)
#  numlist.append(value)

#average = sum(numlist) / len(numlist)
#print('Average', average)




#BEST FRIENDS: STRINGS AND LISTS
#split breaks a string into parts and produces a list of strings.
#We think of these as words. We can access a particular word or loop through all the words.

#abc = 'With three words'
#stuff = abc.split()
#print (stuff)
#print(len(stuff))
#print(stuff[0])

#for w in stuff : 
#  print(w)





#When you do not specify a delimiter, multiple spaces are treated like one delimeter
#You can specify what delimeter character to use in the spliting

#line = 'A lot                  of spaces'
#etc = line.split()
#print(etc)

#line = 'first; second; third'
#thing = line.split ()
#print(thing)
#print(len(thing))

#thing = line.split(';')
#print(thing)

#fhand = open('mbox.txt')
#for line in fhand :
#  line = line.rstrip()
#  if not line.startswith('From: ') : continue
#  words = line.split ()
#  print(words[2])



#THE DOUBLE SPLIT PATTERN
#Sometimes we split a line one way, and then grab one of the pieces of the line and split that
#piece again

#PYTHON DICTONARIES
#WHAT IS A COLLECTION?
#- A collection is nice because we can put more than one value in it and carry them all arround
#in the one convenient package
#-We have a buch of values in a single variable
#-We do this by having more than one plave 'n' the variable
#-We have ways of finding the different places in the variable

#WHAT IS NOT A COLLECTION?
#Most of our vaiables have one value in them - when we put a new value in the variable - 
#the old value is overwriten.

#x = 2
#x = 4
#print(x)

#A STORY OF TWO COLLECTIONS
#list 
#A linear collection of values that stay in order.
#Dictionary
#A 'bag' of values, each with its own label.


#DICTIONARIES
#Dictionaries are Python's most powerful data collection
#Dictionaries allow us to do fast database-like operations in Python
#Dictionaries have different names in different languages.

#Asociative arrays -Perl/PHP
#Propierties or Map or HashMap - Java
#Property Bag -C# / .Net


#DICTIONARIES
#Lists index ther entries based on the position in the list
#Dictionaries are like bads - no order
#So we index the things we put in the dictionary with a 'lookup bag'

#purse = dict()
#purse['money'] = 12
#purse['candy'] = 3
#purse['tissues'] = 75
#print(purse)
#print(purse['candy'])
#purse['candy'] = purse['candy'] + 2
#print(purse)



#COMPARING LISTS AND DICTIONARIES
#Dictionaries are like lists except that they use keys instead of numbers to look up values

#LIST
#lst = list()
#lst.append(21)
#lst.append(183)
#print(lst)
#lst[0] = 23
#print(lst)


#DICTIONARY
#ddd = dict()
#ddd['age'] = 21
#ddd['course'] = 182
#print(ddd)
#ddd['age'] = 23
#print(ddd)

#DIRECTION LITERALS(CONSTANTS)
#Dictionary literals use curly braces and have a list of  key: value pairs
#You can make an empty dictionary using empty curly braces

#jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
#print(jjj)

#ooo = { }
#print(ooo)




#COMMON APLICATIONS OF DICTIONARIES
#MOST COMMON NAME?

#MANY COUNTERS WITH A DICTIONARY
#One common use of dictionaries is counting how often we 'see' something

#ccc = dict()
#ccc['csev'] = 1
#ccc['cwen'] = 1
#print(ccc)

#ccc['cwen'] = ccc ['cwen'] + 1
#print(ccc)


#DICTIONARY TRACEBACKS
#It is an error to reference a key which is not in the dictionary 
#We can use the in operator to see if a key is in the dictionary

#ccc = dict()
#print('csv' in ccc)



#WHEN WE SEE A NEW NAME
#When we enconunter a new name, we nedd to add a new entry in the dictionary and if this the
#second or later time we have seen the name, we simply add one to the count in the dictionary
#under that name

#counts = dict ()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names :
#  if name not in counts :
#    counts[name] = 1
#  else: 
#    counts[name] = counts[name] + 1
#print(counts)




#THE GET METHOD FOR DICTIONARIES
#The pattern of checking to see if a key is already in a dictionary and assuming a default 
#value if the key is not there is so common that there is a method called get() that does this

#Default value if key does not exist (and no Traceback)

#counts = dict ()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names : 
#  counts[name] = counts.get(name, 0) + 1
#print(counts)


