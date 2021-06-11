"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#This line is a function with some_words being the function with a list containing'what', 'does', 'this', 'line', 'do', '?' the [] is used for defining lists and indexing into all collections
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#this will print "word" when "word" is called from the some_words list
for word in some_words:
    print(word)

#this will print "x" when "x" is called from the some_words list
for x in some_words:
    print(x)

#this will print out the list 'some_words'
print(some_words)

#if there is more than 3 words in 'some_words' it will print 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words')

#this will get the information about current operating system (or of the platform)
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
#comes up with platform not defined
