'''
This outline will help solidify concepts from the Conditionals lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a int variable named a. Now make an if statement, and if a is more than
#5, print out "a is more than 5."

# if
x = 5
if x>5:
    print("The x vale is positive")
x = True
if x:
    print('the x value is positive')

#2) Make a boolean variable named b. Now make an if statement, and if b is True
#print out "b is True."
# if
b = 1
if b == 1:
    print("b is true")

#3) Make an int variable named c. Now make an if/elif statement, and if c is 
#more than 0, print "c is positive". Else if c is less than 0, print "c is
#negative".

# if. else-if, else
c = 0
if c < 0:
    print("the c value is positive")
elif c == 0:
    print("the c value is less than zero")
else:
    print("the c value is negative")




#4) Make an int variable named d. Now make an if/elif/else statement, and if 
#d is more than 0, print "d is positive". Else if d is less than 0, print "c is
#negative". Else, print "d is zero".
# if. else-if,else
d = 0
if d > 0:
    print("d is positive")
elif d == 0:
    print("the d value is negative")
else:
    print("d is zero")


#5) Make an if statement with any comparison, with a common SYNTAX error.

f = 1
if f > 3:
    print("f is negative")
