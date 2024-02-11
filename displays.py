#DIFFERENT MENU DISPLAYS

def mainMenuDisplay():
    print(" ---------------------------------------------------------------------------\n" +
          "|                  Welcome to Real Life Currency Skills                     |\n"+
          "|---------------------------------------------------------------------------|\n"+
          "|             A place where learners can expect to learn the                |\n"+
          "|                 ins and outs of handling US currency!                     |\n"+ 
          "|                                                                           |\n"+
          "|   Please enter the corresponding number of desired action and hit enter!  |\n"+
          "|                                                                           |\n"+
          "|                                1) Begin                                   |\n"+
          "|                                2) Settings                                |\n"+
          "|                                3) Exit                                    |\n"+ 
          "|                                4) Help                                    |\n"+  
          " ---------------------------------------------------------------------------" )


def settingsMenuDisplay(selections):
    print( " ---------------------------------------------------------------------------\n" +
           "|                                 Settings                                  |\n"+
           "|---------------------------------------------------------------------------|\n"+
           "|      Please enter coin denominations you would like to use and select     |\n"+
           "|                       complete when you are ready.                        |\n"+
           "|                                                                           |\n"+
          f"|                              1) Half Dollars [{selections[0]}]                          |\n"+
          f"|                              2) Quarters     [{selections[1]}]                          |\n"+
          f"|                              3) Dimes        [{selections[2]}]                          |\n"+  
          f"|                              4) Nickels      [{selections[3]}]                          |\n"+ 
          f"|                              5) Pennies      [{selections[4]}]                          |\n"+ 
           "|                              6) Complete                                  |\n"+ 
           " ---------------------------------------------------------------------------" )
    
def runningAppDisplay(trialAmount):
    print( " ---------------------------------------------------------------------------\n" +
           f"|                                 ${trialAmount}                                     |\n"+
           "|---------------------------------------------------------------------------|\n"+
           "|            Please enter whether the correct value was provided            |\n"+
           "|                                                                           |\n"+
           "|                                1) Correct                                 |\n"+
           "|                                2) Incorrect                               |\n"+
           "|                                3) Exit                                    |\n"+
           " ---------------------------------------------------------------------------" )
    
def helpMenuDisplay():
    helpText = '''
    How to use Real Life Currency Skills:

    From the main menu there there is an option to jump right in by 
    selecting begin or you can go to settings to configure how you will
    be tested.
    

    Settings:

    This menu will display the different currencies available for
    testing, which currently consists of Half Dollars, Quarters,
    Dimes and Pennies. A denomination is selected when the brackets
    to the right of the currency is denoted as [x]. When you have 
    selected the denominations you are wanting to test with enter 6
    to complete your configuration, this will return you to the main
    menu.
    

    Begin:

    Selecting begin will start the testing process with the current
    configuration.If you did not set up a custom configuration the 
    tests will consists of all forms of US change.Prior to beginning
    you will be asked how many trials you would like to run, this will
    be the number of questions you are asked.
    You will select either 
        1)Correct or 2)Incorrect
    for each trial and once you have met your selected number of trials
    you will return back to the main menu. At any time you can exit the
    testing interface by entering 3)Exit

    
    Future Adaptations:

    In the future there will be a full graphical interface with more
    options of testing.
    *ALL current options and utility will remain present within the app*\n\n
    '''




    print(" ---------------------------------------------------------------------------\n" +
          "|                        Real Life Currency Skills                          |\n"+
          " --------------------------------------------------------------------------- \n"+
           helpText +
          "                Enter any key to return to Home Menu                     \n"+  
          " ---------------------------------------------------------------------------" )