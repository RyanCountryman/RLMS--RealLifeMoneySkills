import random
import numpy as np

text_prompts = { #TEXT PROMPTS FOR INPUT VALUES
    1: "Please enter the number of trials you would like to run: ",
    2: "Enter your minimum amount $",
    3: "Enter your maximum amount $",
    4: "Would you like to test with cents? (1:ALL CHANGE 2:ONLY QUARTERS 3:NO CHANGE)"
}

specifier_values = {
    1 : "No cents used",
    2 : "Only Quarters",
    3 : "Only Dimes",
    4 : "Only Nickels",
    5 : "Only Pennies",
    6 : "Cents used"
}





def integerCheck(promptNumber):
    while True:
        if(promptNumber == 2):
            choice = []
            choice.append(input(text_prompts[promptNumber]))
            choice.append(input(text_prompts[promptNumber + 1]))

            if(np.char.isdigit(choice).all() and (int(choice[0]) < int(choice[1]))): #ensures all values are integers and max is larger than min
                choice = map(int,choice)
                break
        elif(promptNumber == 4):
            choice = input(text_prompts[promptNumber])
            if(choice.isdigit() and int(choice) < 4):
                choice = int(choice)
                break

        else:
            choice = input(text_prompts[promptNumber])
            if(choice.isdigit()):
                choice = int(choice)
                break

        print("Please enter a valid input")
    return choice

def randomizer(trials,min,max,specifier):
    trial_values = []
    quarter_Values = [25,50,75] 
    dime_values = [10,20,30,40,50,60,70,80,90] #unique dime values
    nickel_values = [5,15,35,45,55,65,85,95] #unique nickel values

    if(specifier == 1):
        for i in range(trials):
            #trial_values.append(f"${round(random.randrange(min,max) + random.random(),2)}")
            numValue = random.randrange((min + 0.01)*100,max*100)/100
            trial_values.append("${:,.2f}".format(numValue))

    elif(specifier == 2):
        for i in range(trials):
            trial_values.append(f"${random.randrange(min,max)}.{random.choice(quarter_Values)}")
            
    elif(specifier == 3):
        for i in range(trials):
            trial_values.append(f"${random.randrange(min,max)}")



    return trial_values






def main():
    print("Welcome to RL-MoneySkills\nAn application to assist in teaching Real Life money skills!\n")

    trials = integerCheck(1)
    min,max = integerCheck(2)
    #print(trials)
    #print(min,max)
    trial_values = randomizer(trials,min,max,integerCheck(4))
    #trial_values = randomizer(trials,min,max,3)
    print(trial_values)



main()