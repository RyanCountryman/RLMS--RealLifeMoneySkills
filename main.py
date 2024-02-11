#Ryan Countryman; CS361 Real Life Currency Skills
from displays import *
from tools import *

def mainMenuInterface():#Handles user input on Main Menu
    selections = ['x','x','x','x','x']     # [ HD , Q , D , N , P]
   
    exitParam = True
    while exitParam:
        mainMenuDisplay()
        menuSelection = input()
        if(inputValidator(menuSelection,0) == True):
            menuSelection = int(menuSelection)
            exitParam = menuDirector(menuSelection,selections)
        else:
            print("Please enter a valid input")


def runningAppInterface(testVariables): #Handles User Input on App Interface
    results = [testVariables,[-1]] #Creates Two dimensional array to showcase given values and whether user got amount correct
   
    for x in range(len(testVariables)):

        runningAppDisplay("{:.2f}".format(testVariables[x]))
        while True:

            menuSelection = input()
            if(inputValidator(menuSelection,3) == True):
 
                if(int(menuSelection) != 3): #Updates user results in results[1][x] if first trial rights over -1 placeholder in [1][0]
                    menuSelection = int(menuSelection)
                    menuSelection = True if(menuSelection == 1) else False 
                    if x == 0:
                        results[1][x] = menuSelection
                        
                    else:
                        results[1].append(menuSelection)
                        
                    break
                else: return results
            else:
                print("Please Enter a Valid Input")
    return results
   

def settingsMenuInterface(selections):#Handles user input on Settings Menu
    exitParam = True
    while exitParam:
        settingsMenuDisplay(selections)
        menuSelection = input()
        if(inputValidator(menuSelection,1) == True):
            if(int(menuSelection) != 6):
                menuSelection = int(menuSelection)
                selections = settingsHandler(selections,menuSelection - 1)

            else: 
                
                if(all((ele) == ' ' for ele in selections)):
                    print("You need to have at least have one denomination selected!")
                else: exitParam = False
        else:
            print("Please enter a valid input")

    return selections


def helpMenuInterface():#Handles user input on Help Menu
    helpMenuDisplay()
    menuSelection = input()



def menuDirector(src,selections):#Directs user from various menues
    match(src):
        case 1:
            results = runningAppInterface(trialGen(selections))
            print(f"RESULTS:\n {results}") #RESULTS WILL BE SENT TO MICROSERVICE TO BE HANDLED AND SENT BACK VIA TXT/JSON WILL BE SENT TO PARSER FOR DISPLAY PURPOSES

        case 2:
            settingsMenuInterface(selections)
        case 3:
            return False
        case 4:
            helpMenuInterface()
    return True




def main():
    mainMenuInterface()

if __name__ == '__main__' :
    try:
        main()
    except:
        print("Error")