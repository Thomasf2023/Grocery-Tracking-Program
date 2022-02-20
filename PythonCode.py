import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def displayMenu(): #Function that prints the display menu
    print()
    print("-----------------------------------------------------------------------")
    print("* Please enter 1, 2, 3, or 4 to make your selection.                  *")
    print("* (1): View list of items purchased on a given day with quantity sold *")
    print("* (2): View total purchases of item on a given day                    *")
    print("* (3): View sales histogram                                           *")
    print("* (4): Exit Program                                                   *")
    print("-----------------------------------------------------------------------")

def individualItemQuantity(): #function that reads the file and prints Individual item quantity
    inputList = []

    myFile = open(r"U:\CS-210-Python-C++\Release\ProjectThreeInput.txt","r")
    inputList = myFile.read()
    
    spinach = inputList.count("Spinach")
    radishes = inputList.count("Radishes")
    broccoli = inputList.count("Broccoli")
    peas = inputList.count("Peas")
    cranberries = inputList.count("Cranberries")
    potatoes = inputList.count("Potatoes")
    cucumbers = inputList.count("Cucumbers")
    peaches = inputList.count("Peaches")
    zucchini = inputList.count("Zucchini")
    cantaloupe = inputList.count("Cantaloupe")
    beets = inputList.count("Beets")
    cauliflower = inputList.count("Cauliflower")
    onions = inputList.count("Onions")
    yams = inputList.count("Yams")
    apples = inputList.count("Apples")
    celery = inputList.count("Celery")
    limes = inputList.count("Limes")
    garlic = inputList.count("Garlic")
    pumpkins = inputList.count("Pumpkins")
    pears = inputList.count("Pears")
   

    print("Individual Item Quantity:")
    print("Spinach {}:".format(spinach))
    print("Radishes {}:".format(radishes))
    print("Broccoli {}:".format(broccoli))
    print("Peas {}:".format(peas))
    print("Cranberries {}:".format(cranberries))
    print("Potatoes {}:".format(potatoes))
    print("Cucumbers {}:".format(cucumbers))
    print("Peaches {}:".format(peaches))
    print("Zucchini {}:".format(zucchini))
    print("Cantaloupe {}:".format(cantaloupe))
    print("Onions {}:".format(onions))
    print("Yams {}:".format(yams))
    print("Apples {}:".format(apples))
    print("Celery {}:".format(celery))
    print("Limes {}:".format(limes))
    print("Garlic {}:".format(garlic))
    print("Pumpkins {}:".format(pumpkins))
    print("Pears {}:".format(pears))
   

def givenItemQuantity(v): #Function that returns item quantity

    
    inputList = []

    myFile = open(r"U:\CS-210-Python-C++\Release\ProjectThreeInput.txt","r")
    inputList = myFile.read()

    itemQuantity = inputList.count(v)

    return itemQuantity

def fequencyFileCreator(): #Function to create the fequency file
    
    inputList = []

    myFile = open(r"U:\CS-210-Python-C++\Release\ProjectThreeInput.txt","r")
    inputList = myFile.read()

    spinach = inputList.count("Spinach")
    radishes = inputList.count("Radishes")
    broccoli = inputList.count("Broccoli")
    peas = inputList.count("Peas")
    cranberries = inputList.count("Cranberries")
    potatoes = inputList.count("Potatoes")
    cucumbers = inputList.count("Cucumbers")
    peaches = inputList.count("Peaches")
    zucchini = inputList.count("Zucchini")
    cantaloupe = inputList.count("Cantaloupe")
    beets = inputList.count("Beets")
    cauliflower = inputList.count("Cauliflower")
    onions = inputList.count("Onions")
    yams = inputList.count("Yams")
    apples = inputList.count("Apples")
    celery = inputList.count("Celery")
    limes = inputList.count("Limes")
    garlic = inputList.count("Garlic")
    pumpkins = inputList.count("Pumpkins")
    pears = inputList.count("Pears")

    
    myFile.close()
    

    
   
    myNewFile = open(r'U:\CS-210-Python-C++\CS-210-Python-C++\frequency.txt', 'w')

    myNewFile.write("Spinach: ")
    myNewFile.write("%s" % spinach)
    myNewFile.write("\nRadishes: ")
    myNewFile.write(str(radishes))
    myNewFile.write("\nBroccoli: ")
    myNewFile.write(str(broccoli))
    myNewFile.write("\nPeas: ")
    myNewFile.write(str(peas))
    myNewFile.write("\nCranberries: ")
    myNewFile.write(str(cranberries))
    myNewFile.write("\nPotatoes: ")
    myNewFile.write(str(potatoes))
    myNewFile.write("\nCucumbers: ")
    myNewFile.write(str(cucumbers))
    myNewFile.write("\nPeaches: ")
    myNewFile.write(str(peaches))
    myNewFile.write("\nZucchini: ")
    myNewFile.write(str(zucchini))
    myNewFile.write("\nCantaloupe: ")
    myNewFile.write(str(cantaloupe))
    myNewFile.write("\nBeets: ")
    myNewFile.write(str(beets))
    myNewFile.write("\nCauliflower : ")
    myNewFile.write(str(cauliflower))
    myNewFile.write("\nOnions: ")
    myNewFile.write(str(onions))
    myNewFile.write("\nYams: ")
    myNewFile.write(str(yams))
    myNewFile.write("\nApples: ")
    myNewFile.write(str(apples))
    myNewFile.write("\nCelery: ")
    myNewFile.write(str(celery))
    myNewFile.write("\nLimes: ")
    myNewFile.write(str(limes))
    myNewFile.write("\nGarlic: ")
    myNewFile.write(str(garlic))
    myNewFile.write("\nPumpkins: ")
    myNewFile.write(str(pumpkins))
    myNewFile.write("\nPears: ")
    myNewFile.write(str(pears))



    myNewFile.close()

def histrogramCreator(): #This function will call the file and create a histogram using recycled code from an earlier function.
    inputList = []

    astrick = "*"

    myFile = open(r"U:\CS-210-Python-C++\Release\ProjectThreeInput.txt","r")
    inputList = myFile.read()
    
    spinach = inputList.count("Spinach")
    radishes = inputList.count("Radishes")
    broccoli = inputList.count("Broccoli")
    peas = inputList.count("Peas")
    cranberries = inputList.count("Cranberries")
    potatoes = inputList.count("Potatoes")
    cucumbers = inputList.count("Cucumbers")
    peaches = inputList.count("Peaches")
    zucchini = inputList.count("Zucchini")
    cantaloupe = inputList.count("Cantaloupe")
    beets = inputList.count("Beets")
    cauliflower = inputList.count("Cauliflower")
    onions = inputList.count("Onions")
    yams = inputList.count("Yams")
    apples = inputList.count("Apples")
    celery = inputList.count("Celery")
    limes = inputList.count("Limes")
    garlic = inputList.count("Garlic")
    pumpkins = inputList.count("Pumpkins")
    pears = inputList.count("Pears")

    print("---------------------------------------------------")
    print()
    print("Sales Histrogram:")
    print()
    print("Spinach     " + (astrick *  spinach))
    print("Radishes    " + (astrick * radishes))
    print("Broccoli    " + (astrick * broccoli))
    print("Peas        " + (astrick * peas))
    print("Cranberries " + (astrick * cranberries))
    print("Potatoes    " + (astrick * potatoes))
    print("Cucumbers   " + (astrick * cucumbers))
    print("Peaches     " + (astrick * peaches))
    print("Zucchini    " + (astrick * zucchini))
    print("Cantaloupe  " + (astrick * cantaloupe))
    print("Beets       " + (astrick * beets))
    print("Cauliflower " + (astrick * cauliflower))
    print("Onions      " + (astrick * onions))
    print("Yams        " + (astrick * yams))
    print("Apples      " + (astrick * apples))
    print("Celery      " + (astrick * celery))
    print("Limes       " + (astrick * limes))
    print("Garlic      " + (astrick * garlic))
    print("Pumpkins    " + (astrick * pumpkins))
    print("Pears       " + (astrick * pears))
    print()
    print("---------------------------------------------------")

