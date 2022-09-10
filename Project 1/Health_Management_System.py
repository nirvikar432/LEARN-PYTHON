def getDate():
    import datetime
    x = datetime.datetime.now()
    return x.strftime("%c")

def logfile(userChoice,userInput):
    if(userChoice == 1 and userInput == 1):#Nirvikar Food
        foodLog(userChoice)
    elif(userChoice == 2 and userInput == 1):#Mrigank Food
        foodLog(userChoice)
    elif(userChoice == 3 and userInput == 1):#Kumar Food
        foodLog(userChoice)
    if(userChoice == 1 and userInput == 2):#Nirvikar Drink
        drinkLog(userChoice)
    elif(userChoice == 2 and userInput == 2):#Mrigank Drink
        drinkLog(userChoice)
    elif(userChoice == 3 and userInput == 2):#Kumar Drink
        drinkLog(userChoice)

def showFile(userChoice,userInput):
    if(userChoice == 1 and userInput == 1):#Nirvikar Food
        foodShow(userChoice)
    elif(userChoice == 2 and userInput == 1):#Mrigank Food
        foodShow(userChoice)
    elif(userChoice == 3 and userInput == 1):#Kumar Food
        foodShow(userChoice)
    if(userChoice == 1 and userInput == 2):#Nirvikar Drink
        drinkShow(userChoice)
    elif(userChoice == 2 and userInput == 2):#Mrigank Drink
        drinkShow(userChoice)
    elif(userChoice == 3 and userInput == 2):#Kumar Drink
        drinkShow(userChoice)

def foodLog(userName):
    if(userName == 1):#Nirvikar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p1food.txt", "a") as f:
            foodEntry = input("Enter food item name for Nirvikar : ")
            time = str(getDate())
            f.write(f"{foodEntry} taken at time {time}\n")
            print("successfully written")

    elif(userName == 2):#Mrigank
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p2food.txt", "a") as f:
            foodEntry = input("Enter food item name for Mrigank : ")
            time = str(getDate())
            f.write(f"{foodEntry} taken at time {time}\n")
            print("successfully written")
        
    elif(userName == 3):#Kumar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p3food.txt", "a") as f:
            foodEntry = input("Enter food item name for Kumar : ")
            time = str(getDate())
            f.write(f"{foodEntry} taken at time {time}\n")
            print("successfully written")

def drinkLog(userName):
    if(userName == 1):#Nirvikar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p1drink.txt", "a") as f:
            drinkEntry = input("Enter drink item name for Nirvikar : ")
            time = str(getDate())
            f.write(f"{drinkEntry} taken at time {time}\n")
    elif(userName == 2):#Mrigank
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p2drink.txt", "a") as f:
            drinkEntry = input("Enter drink item name for Mrigank : ")
            time = str(getDate())
            f.write(f"{drinkEntry} taken at time {time}\n")
        
    elif(userName == 3):#Kumar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p3drink.txt", "a") as f:
            drinkEntry = input("Enter drink item name for Kumar : ")
            time = str(getDate())
            f.write(f"{drinkEntry} taken at time {time}\n")
    
def foodShow(userName):
    if(userName == 1):#Nirvikar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p1food.txt") as f:
            content = f.read()
            print(content)

    elif(userName == 2):#Mrigank
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p2food.txt") as f:
            content = f.read()
            print(content)
        
    elif(userName == 3):#Kumar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p3food.txt") as f:
            content = f.read()
            print(content)
            
def drinkShow(userName):
    if(userName == 1):#Nirvikar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p1drink.txt") as f:
            content = f.read()
            print(content)
    elif(userName == 2):#Mrigank
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p2drink.txt") as f:
            content = f.read()
            print(content)
        
    elif(userName == 3):#Kumar
        with open("C:\\Users\\NIRVIKAR\Documents\\Learn Python\\Project 1\\p3drink.txt") as f:
            content = f.read()
            print(content)

while(True):
    print("\t\tWelcome to Health management System\t\t")
    userChoice = int(input('''
                            Press 1 : Nirvikar
                            Press 2 : Mrigank
                            Press 3 : Kumar    
                            Press 4 : Exit  \n'''))
    if userChoice == 4:
        break

    logShow = int(input('''
                            Press 1 : Add Log
                            Press 2 : Preview log   \n'''))
    if(logShow == 1):
        userInput = int(input('''
                                Press 1 : Food
                                Press 2 : Drink   \n'''))
        logfile(userChoice, userInput)
    elif(logShow == 2):
        userInput = int(input('''
                                Press 1 : Food
                                Press 2 : Drink   \n'''))
        showFile(userChoice,userInput)




