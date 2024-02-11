import random

def settingsHandler(selections,menuSelection):#Handles change in user selection on settings menu
    if(selections[menuSelection] == 'x'):
        selections[menuSelection] = ' '
    else:
        selections[menuSelection] = 'x'
    return selections



def inputValidator(input, src):
    match(src):
        case 0: #Main Menu validation expected inputs 1-4
            if(input.isdigit()):
                return True if (0 < int(input) < 5) else False
            else: return False
        case 1: #Settings Menu Validation expected inputs 1-6
            if(input.isdigit()):
                return True if (0 < int(input)< 7 )else False
            else: return False
        case 2: #Trial Selection expected inputs 1-10
            if(input.isdigit()):
                return True if (0 < int(input) < 11) else False
        case 3: #App Running Validation expected inputs 1-3
            if(input.isdigit()):
                return True if (0 < int(input) < 4) else False



def randomGen(selections):
    #Defining Coin Limits
    half_dollar_limit = 2 if(selections[0] == 'x') else 0 #if HD selected values:(ct: 0 -> 2) 0.00, 0.50, 1.00 
    quarter_limit = 4 if(selections[1] == 'x') else 0     #if Q selected values:(ct: 0 -> 4) 0.00,0.25,0.50,0.75,1.00 
    dime_limit = 10 if(selections[2] == 'x') else 0       #if D selected values:(ct: 0 -> 10) 0.00,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00
    nickel_limit = 20 if(selections[3] == 'x') else 0     #if N selected values:(ct: 0 -> 20) 0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00
    penny_limit = 100 if(selections[4] == 'x') else 0     #if P selected values:(ct: 0 -> 100) 0.00 -> 1.00

    total = 1.1

    while not(0.00 < total <= 1.00):
        half_dollar_quantity = random.randint(0,half_dollar_limit)
        quarter_quantity = random.randint(0,quarter_limit)
        dime_quantity = random.randint(0,dime_limit)
        nickel_quantity = random.randint(0,nickel_limit)
        penny_quantity = random.randint(0,penny_limit)

        half_dollar_value = 0.5 * half_dollar_quantity
        quarter_value = 0.25 * quarter_quantity
        dime_value = 0.10 * dime_quantity
        nickel_value = 0.05 * nickel_quantity
        penny_value = 0.01 * penny_quantity

        total = half_dollar_value + quarter_value + dime_value + nickel_value + penny_value

    return round(total,2)

def trialGen(selections): #Selects number of trials and fills trial array
    numberTrials = input("How many trials would you like to run? Enter a number between 1 to 10\n")
    while True:
        if not(inputValidator(numberTrials,2)):
            print("Please Enter a Valid Input between 1 and 10")
            numberTrials = input()
        else: break
    
    trials = []        
    for i in range(int(numberTrials)):
        trials.append(randomGen(selections))
    return trials