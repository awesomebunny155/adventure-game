#-----------------------------------------------------------------------------
# Name:        Harry Potter: Lost in Forbidden Forest Edition (assignment.py)
# Purpose:     This adventure game is composed of chronological events from Harry Potter
# that attempts to spark a new and interesting storyline for users. It composes of
# a quiz bowl format with easy and expert questions wherin the user will utilize
# context clues from the previous levels to move on further in the story. Towards the
# increasing levels, easy and expert sides of the story will connect to defeat Harry Potter's
# greatest enemy, Voldemort. As the user tailors their story, the game allows them to filter
# out using various difficulty level and provides them with multiple chances to advance. If the
# difficulty level is chosen, then the user will have to advance to success despite Harry's
# senseless actions. 
# Author:      Harini Karthik
# Created:     18-Feb-2021
# Updated:     22-Feb-2021 
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# STEP 1: Import the required libraries 
import random
import time
import PySimpleGUI as sg
sg.theme('Light Blue 3')

# STEP 2: Define a function for each of the level
# Level 1 is defined with easy and expert parameter
def level1(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['After meeting Graup, will Harry Potter use the levitation charm to defeat him?',
                'Will Harry Potter bring up severe problems with the spiders by opposing Graup?']    
    arrHardQ = ['After meeting Graup, will Harry Potter diplomatically try the "throwing off wand" spell that he learned in class?',
     'Did Harry annoy Graup in attempt to make friends with him?']
    
    # Answers are set using True or false statement
    arrEasyAns=[True, True]
    arrHardAns = [True, False]
    
    # Random int is used to get a question from the array 
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]
    
# Level 2 is defined with easy and expert parameter
def level2(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['After encountering the spiders, are they angry at Harry Potter?', 
    'Are spiders angry at Harry because of his reputation?']    
    arrHardQ = ['Does Harry run away from Graup?',
     'Did Harry get invited by Graup\'s family for dinner?']
    
    # Answers are set using True or false statement
    arrEasyAns=[True, False]
    arrHardAns = [True, False]
  
    # Random int is used to get a question from the array     
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]
    
# Level 3 is defined with easy and expert parameter
def level3(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['After being directed to the chamber of secrets by angry creature, does Harry find more in Newt\'s suitcase?', 
    'Will Harry Potter find Tom Riddle waiting for him in the Chamber of Secrets?']    
    arrHardQ = ['After being directed to the arena by the angry creature, does Harry defeat the dragons with his quiddich talent?',
     'Will Harry Potter travel in a portkey similar to that of Triwizard Tournament?']
    
    # Answers are set using True or false statement
    arrEasyAns=[False, False]
    arrHardAns = [False, True]
    
    # Random int is used to get a question from the array  
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]

# Level 4 is defined with easy and expert parameter
def level4(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['Does Harry Potter become a leader to the fantastic beasts?', 
    'Does Harry Potter attack the large niffler who was trying to help him?']    
    arrHardQ = ['Does Harry Potter get helped from cursed Nagini?',
     'Will Harry Potter fail the mission by not believing Nagini\'s words?']
    
    # Answers are set using True or false statement
    arrEasyAns=[True, False]
    arrHardAns = [True, False]
  
    # Random int is used to get a question from the array    
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]

# Level 5 is defined with easy and expert parameter
def level5(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['Does Harry destroy Nagini\'s Horcrux with the help of fantastic beast army to defeat Voldemort?', 
    'Will Harry get digested by these creatures??']    
    arrHardQ = ['Does Harry lift the curse of Nagini by fighting with these creatures?',
     'Is the ememy of Harry Potter going to be Voldemort in form of Grindlewald?']
    
    # Answers are set using True or false statement
    arrEasyAns=[True, False]
    arrHardAns = [False, True]
   
    # Random int is used to get a question from the array     
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]

# Level 6 is defined with easy and expert parameter
def level6(easy, expert):
    time.sleep(1.5)
    # Arrays are set for both the parameters
    arrEasyQ = ['Does Horcrux help him defeat another form of Voldemort?', 
    'Are his friends okay?']    
    arrHardQ = ['Does Harry Potter\'s misbehavior with Graup make the fantastic beasts betray him? ',
     'Does Nagini\'s curse get lifted with Grindelwald\'s defeat?']
    
    # Answers are set using True or false statement
    arrEasyAns=[True, True]
    arrHardAns = [True, True]
  
    # Random int is used to get a question from the array    
    if easy == True:
        num = random.randint(0, len(arrEasyQ)-1)
        return arrEasyQ[num], arrEasyAns[num]
    else:
        num = random.randint(0, len(arrHardQ)-1)
        return arrHardQ[num], arrHardAns[num]   

# Define the main function where the question is not already answered and initial level is 1
def main():
    sAnswer = False
    isQuestionAnswered = False
    nLevelNo = 1
    
    #STEP 3: Layout the GUI include the text and radio buttons (option menu)
    # Image Credit: Pottermore from Pintrest (Author: Lucie)
    layout = [  [sg.Text("Welcome to Harry Potter\'s Adventures in Forbidden Forest!!", size=(50, 1), justification='center', font=("Courier 10",14), relief=sg.RELIEF_RIDGE)],
                [sg.Image('C:\\GitHub\\HaltonSchool\\mini-adventure-awesomebunny155\\Assets\\harryBroom.png', size=(275,275)), sg.Frame(layout=[
                    [sg.Radio('Level 1', "RADIO2",default=True, size=(15,1), key="-L1-"), sg.Radio('Level 2', "RADIO2",default=True, size=(15,1), key="-L2-"), sg.Radio('Level 3', "RADIO2",default=True, size=(15,1), key="-L3-"), sg.Radio('Level 4', "RADIO2",default=True, size=(15,1), key="-L4-"), sg.Radio('Level 5', "RADIO2",default=True, size=(15,1), key="-L5-"),sg.Radio('Level 6', "RADIO2",default=True, size=(15,1), key="-L6-")],
                    [sg.Radio('Easy', "RADIO1", default=True, size=(15,1), key="-EASY-"), sg.Radio('Expert', "RADIO1", key="-EXPERT-")]], title='Options',title_color='#A613B1', relief=sg.RELIEF_SUNKEN, tooltip='Use the menu to set the game mode in each level ')],
                [sg.Text(size=(100,1), key='_OUT', justification='center', font=("Helvetica", 15)) ],
                [sg.Text(size=(100,1), key='_ERR', justification='center', font=("Helvetica", 15)) ],
                [sg.Button('PROCEED')],
                [sg.Button('TRUE'), sg.Button('FALSE'), sg.Button('QUIT') ]]
    
    # STEP 4: Create the window with the title and align to the layout
    window = sg.Window('Harry Potter\'s Adventures: Lost in Forbidden Forest Edition', layout)  
    
    # STEP 5: Set up the event loop and quit button (break condition)
    while True:             
        event, values_list = window.read()
        if event == sg.WIN_CLOSED or event == 'QUIT':            
            break

        # STEP 6: The question answered is set as false when proceeding to the next level (Refreshing)         
        if event == 'PROCEED':
            isQuestionAnswered = False
            
            # Set the conditions for each level, including the level number
            if values_list["-L1-"] == True and nLevelNo ==1:
                sMsg, sAnswer = level1(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                
            elif values_list["-L2-"] == True and nLevelNo ==2:
                sMsg, sAnswer = level2(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                
            elif values_list["-L3-"] == True and nLevelNo ==3:
                sMsg, sAnswer = level3(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                
            elif values_list["-L4-"] == True and nLevelNo ==4:
                sMsg, sAnswer = level4(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                
            elif values_list["-L5-"] == True and nLevelNo ==5:
                sMsg, sAnswer = level5(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                
            elif values_list["-L6-"] == True and nLevelNo ==6:
                sMsg, sAnswer = level6(values_list["-EASY-"], values_list["-EXPERT-"])
                sErrorMsg = ''
                        
            else:
                time.sleep(1.5)
                sMsg = "Check your Level Status"
                sErrorMsg = "Your Current Level is "+ str(nLevelNo)
           
                
     # STEP 7: Define the event when true or false button is clicked on 
        if event == 'TRUE':
            #Set an error message condition when the question is already answered
            if isQuestionAnswered == True:
                sErrorMsg = "You have already attempted this question!"
                
            # If the answer is true, it will print the correct status and increment the level by 1
            elif sAnswer == True:
                sErrorMsg = 'That\'s Right :) Choose the next level to proceed'
                isQuestionAnswered = True
                nLevelNo +=1
                sAnswer = False #Resetting the answer so that the cheat code doesn't work 
            
            # If the answer is wrong, it will print out the message 
            else:
                sErrorMsg = 'Nope...Choose another question :('
                isQuestionAnswered = True
                
        
        if event == 'FALSE':
            #Set an error message condition when the question is already answered
            if isQuestionAnswered == True:
                sErrorMsg = "You have already attempted this question!"
                
            # If the answer is correct (matches with False), it will print the correct status and increment the level by 1
            elif sAnswer == False:
                sErrorMsg = 'That\'s Right :) Choose the next level to proceed'
                isQuestionAnswered = True
                nLevelNo +=1
                sAnswer = True   #Resetting the answer so that the cheat code doesn't work 
                
            # If the answer is wrong, it will print out the message 
            else:
                sErrorMsg = 'Nope...Choose another question :('
                isQuestionAnswered = True
        
        # STEP 8: Updating the window with the status message and question
        window['_OUT'].update(sMsg, text_color='blue')
        window['_ERR'].update(sErrorMsg, text_color='#A613B1')
    window.close()
# Driver code for executing main
if __name__ == '__main__':
    main()