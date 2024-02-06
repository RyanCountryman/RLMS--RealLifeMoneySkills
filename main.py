#Ryan Countryman; CS361 Real Life Currency Skills

def mainMenuInterface():
    print(" ------------------------------------------------------------\n" +
          "|            Welcome to Real Life Currency Skills            |\n"+
          "|------------------------------------------------------------|\n" +
          "|   Please enter the corresponding number of desired action  |\n"+
          "|                                                            |\n"+
          "|                        1) Begin                            |\n"+
          "|                        2) Settings                         |\n"+
          "|                        3) Exit                             |\n"+  
          " ------------------------------------------------------------" )
    
    exitParam = True

    while exitParam:
        menuSelection = input()
        if(inputValidator(menuSelection,0) == True):
            menuSelection = int(menuSelection)
            exitParam = menuDirector(menuSelection)
        else:
            print("Please enter a valid input")



def inputValidator(src, locale):
    match(locale):
        case 0: #Main Menu validation expected inputs 1-3
            if(src.isdigit()):
                return True if (0 < int(src) < 4) else False
            else: return False


#TODO Craft Settings and Running App Display

def menuDirector(src):
    print("HELLOFROMMENUDIRECT")
    match(src):
        case 1:
            print("BEGIN APPLICATION")
        case 2:
            print("OPEN SETTINGS MENU")
        case 3:
            print("EXIT APPLICATION")

def main():
    mainMenuInterface()





if __name__ == '__main__' :
    try:
        main()
    except:
        print("Error")