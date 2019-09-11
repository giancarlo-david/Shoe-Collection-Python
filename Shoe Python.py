def main():
    shoeList = []
    exitBool = False

    while (exitBool == False):
        # Print the main menu and its options
        print("\tMain Menu")
        print("1. Add Shoe(s)")
        print("2. Remove Shoe(s)")
        print("3. Show Count")
        print("4. Sort List")
        print("5. Show List")
        print("6. Import List")
        print("7. Export List")
        print("8. Exit")
        

        # Get user input for main menu choice
        choice = input("\nPlease enter the number of the option you want to select: ")

        # If statement to validate user input
        if (choice.isdigit() == False):
            print("\nPlease enter a number")

        # Elif statement when user input is a digit    
        elif (choice.isdigit() == True):
            
            # If statement for add shoes option
            if (choice == '1'):
                print("\nTime to add some shoes!")
                # Call add shoe function
                addShoe(shoeList)

            # Elif statement for remove shoes option
            elif (choice == '2'):
                print("\nTime to remove some shoes!")
                # Remove shoe function
                removeShoe(shoeList)

            elif (choice == '3'):
                print("\nHere's the current count")
                showCount(shoeList)
                
            elif (choice == '4'):
                print("\nSorting List...")
                # Sort list function
                sortList(shoeList)
                
            # Elif statement for show list option    
            elif (choice == '5'):
                print("\nHere is the current list:")
                # Show List function
                showList(shoeList)
                
            elif (choice == '6'):
                print("\nImporting list...")
                # Import List function
                importList(shoeList)
                
            elif (choice == '7'):
                print("\nExporting list...")
                # Export list function
                outputToTxt(shoeList)
                
            # Elif statement for exit option    
            elif (choice == '8'):
                print("\nExiting program...")
                exitBool = True


                
            # Else statement to catch invalid input    
            else:
                print("\nPlease enter a valid number option.")

# Definition of function to add shoes to list (1)
def addShoe(shoeList):
    
    # Get number of shoes to add from the user
    numberToAdd = str(input("\nHow many shoes would you like to add? "))
    
    # User input validation
    while not numberToAdd.isdigit():
        numberToAdd = str(input("\nInput Invalid\nHow many shoes would you like to add? "))

    numberToAdd = int(numberToAdd)    
    print("Adding", numberToAdd,  "shoes...")
    
    # For loop to add all the number of shoes designated to add
    for x in range (numberToAdd):
        brand = input("\nEnter the brand of shoe #" + str(x + 1) + ": ")
        model = input("Enter the model of shoe #" + str(x + 1) + ": ")
        colorway = input("Enter the colorway of shoe #" + str(x + 1) + ": ")
        shoeList.append(brand + ' ' + model + ' ' + colorway)
    print("\nFinished adding shoes!\n")

# Definition of function to remove shoes from list (2)
def removeShoe(shoeList):
    
    # Get number of shoes to remove from user
    numberToRemove = str(input("\nHow many shoes would you like to remove? "))
    
    # User input validation
    while not numberToRemove.isdigit():
        numberToRemove = str(input("\nInput Invalid\nHow many shoes would you like to remove? "))

    numberToRemove = int(numberToRemove)
    print("Removing", numberToRemove, "shoes...")

    # For loop to remove all the number of shoes designated to remove
    for x in range(numberToRemove):
        removeShoe = int(input("\nEnter shoe #" + str (x+1) + " to remove (Shoe # when shown in list): "))
        shoeList.pop(removeShoe - 1)
        
        
    print("\nFinished removing shoes!\n")

# Definition of function to show count (3)
def showCount(shoeList):

    print("Total count: ", len(shoeList), "\n")
    # Was working on showCount showing how many of each brand is in your collection, postponed for python right now
    #  will end up implementing in C++ version first
    #print("Nike: ", shoeList.count('Nike'), "\tJordan: ", shoeList.count('Jordan'),\
    #      "\tAdidas: ", shoeList.count('Adidas'))
    #print("Asics: ", shoeList.count('Asics'), "\tConverse: ", shoeList.count('Converse'),\
    #      "\tVans: ", shoeList.count('Vans'))
    #print("Puma: ", shoeList.count('Puma'), "\tNew Balance: ", shoeList.count('New Balance'),\
    #      "\tSperry: ", shoeList.count('Sperry'))
    #print("Cole Haan: ", shoeList.count('Cole Haan'), "\tAldo: ", shoeList.count('Aldo'))

# Definition of function to sort list (4)
def sortList(shoeList):

    # Sort list
    shoeList.sort()
    print("\nList has been sorted!\n")

# Definition of function to print list (5)
def showList(shoeList):
    y = len(shoeList)
    for x in range (y):
        print((x+1), ":", shoeList[x])
    print("\nThese are all the shoes in the current list\n")

# Definition of function to import list (6)
def importList(shoeList):
    # Delete Current list to import new list in a clean slate
    del shoeList[:]
    
    # Get user input for file name and open file
    nameFile = input("\nWhat is the name of the file we are importing? [Exclude .txt]: ")
    importFile = open(nameFile + ".txt")

    # For loop to import file line by line and truncate the newline
    for line in importFile.readlines():
        temp = line[:-1]
        shoeList.append(temp)

    # Close import file
    importFile.close()
    print("\nFile imported!\n")
    
# Definition of function to output list to file (7)
def outputToTxt(shoeList):

    # Get length of list, get user input for file name, and open file
    y = len(shoeList)
    nameFile = input("\nWhat do you want the file to be named? ")
    outputFile = open(nameFile + ".txt", "w")

    # For loop to output list line by line
    for x in range (y):
        outputFile.write(shoeList[x] + "\n")
    outputFile.close()
    print("\nFile printed!\n")
    
main()
