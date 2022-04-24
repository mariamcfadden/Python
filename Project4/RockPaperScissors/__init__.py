'''
Created on Apr 22, 2022

@author: Maria McFadden
'''

#import random
import random
from random import choice

#Make a boolean variable called KeepPlaying to track whether they want to 
#keep playing and set it to True

keepPlaying = True
userScore = 0
cpuScore = 0


#LOOP: Make a game loop that continues while keepPlaying is true
    #Print out a statement to welcome the user to the game
while keepPlaying == True:
    print("Welcome to Rock Paper Scissors")
       
       
    
        #Make variables called userScore and cpuScore to track scores, set to 0
   
        
        #LOOP: Make a loop that continues while the userScore or cpuScore is 
        #less than 2
            #Use input() to get a choice from the user (rock, paper or scissors).
            #Store the choice in variable. Use .lower() to make the users choice
            #all lower case
    while userScore < 2 or cpuScore < 2:
        userChoice = input("Enter Choice (Rock, Paper, Scissors)")
        userChoice = userChoice.lower()
    
        
                #Make a list of choices, then use random.choice() to get a random
                #choice for the cpu. Store the choice in a variable.
        possibleChoice = ["rock", "paper", "scissors"] 
        cpuChoice = random.choice(possibleChoice)   
           
                #Make a if/elif/else statement to check the users input against the
                #cpu's choice:        
                #NOTE: you will have to compare the users choice and the cpu choice to
                #"rock", "paper", and "scissors" separately and combine with logical 
                #operators. EXAMPLE of a tie:
        '''
         if((user == "rock" and cpu == "rock") or (user == "paper" and cpu
         == "paper" or (user == "scissors" and cpu =="scissors")):
                 
        print("DRAW")
             print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
         '''
                
                #if the user won add one to the users score then print out the score
                #"User: [#]"
                
                #else if (elif) the computer won, add one to the computer's score then
                #print out the scores...
                
                #else if is a draw print "DRAW" then print out the scores...   
                
                #else if the user entered 'q', then end the round, and the game loop
                #Use the break statement to end the round. Make keepPlaying equal False
                
                #else the user didn't enter an accepted input, print "not an option,
                #try again,"
        if userChoice.lower() == "q":
            break
        elif userChoice == cpuChoice:
            print("draw")
            print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
        elif userChoice == "rock": 
            if cpuChoice == "scissors":
                print("Rock beats scissors, you win.")
                userScore += 1
            else: 
                print("Paper beats rock, you lose.")
                cpuScore += 1
        elif userChoice == "paper":
            if cpuChoice == "rock":
                print("Paper beats rock, you win.")
                userScore += 1
            else:
                print("Scissors beats paper, you lose")
                cpuScore += 1 
        elif userChoice == "scissors":
            if cpuChoice == "paper":
                print("Scissors beats paper, you win.")
                userScore += 1
            else:
                print("Rock beats scissors you lose")
                cpuScore += 1
        else: 
            print("Not an option, try again.")
            break
        
        
                
                
                
            #print out thank you message 
            #print out who won
    keepPlaying = False
    print("Thank you for playing!")
    if userScore == 2:
        print("User won!")
    elif cpuScore == 2:
        print("Computer won!")
    
    print(f"User's final score {userScore}. Computer's final score {cpuScore}.")
    
            #If the user score is 2, then the user won
                #code
            #elif the cpuScore is 2, then the cpu won
                #code
            #print out the final scores 
            
            
    
    
    
    
    






