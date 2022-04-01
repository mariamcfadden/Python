'''
Created on Apr 1, 2022

@author: Maria McFadden
'''
#set counter to zero
counter = 0 
#Q1
answer1 = "A"
val1 = input("1) What is the powerhouse of the cell?\n"\
   "\tA) mitochondria B) nucleus C) ribosome")


if val1.upper() == answer1:
    print("Correct")
    counter += 1
else:
    print ("Incorrect, the correct answer is A.")

#Q2
answer2 = "C"
val2 = input("2) How many states comprise the United States?\n"\
    "\t  A) 13 B) 45 C) 50")

if val2.upper() == answer2:
    print("Correct")
    counter += 1
else:
    print ("Incorrect, the correct answer is C.")
#Q3   
answer3 = "A"
val3 = input("3) In y = mx + b, what does m stand for?\n"\
    "\t A) slope B) output C) I don't understand math")

if val3.upper() == answer3:
    print("Correct")
    counter += 1
else:
    print ("Incorrect, the correct answer is A.")
#Q4
answer4 = "C"
val4 = input("4) In English, a person, place or thing is called:\n"\
    "\t A) verb B) adjective C) noun")

if val4.upper() == answer4:
    print("Correct")
    counter += 1
else:
    print ("Incorrect, the correct answer is C.")

print("You got ", counter, "out of 4.")
