#  Exercise1: Write a for loop so that every item in the list is printed.
def exercise1():
    print("Given a list, print out all the items inside the list.")
    animal = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
    for i in animal:
        print(i)


#  Exercise2: Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
def exercise2():
    print("Given a name list, write a for loop which print 'Hello!, ' plus each name in the list.")
    name = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
    for i in name:
        print("Hello!,", i)


#  Exercise3:Write a for loop that iterates through a string and prints every letter.
def exercise3():
    print("Given a string, Write a for loop that iterates through a string and prints every letter.")
    lady = "Antarctica"
    for i in lady:
        print(i)


# Exercise4: code a counter variable named c is increased by one each time loop iterates.
def exercise4():
    print("Given a string, code a counter variable named c is increased by one each time loop iterates.")
    text = "Civilization"
    c = 0
    for i in text:
        c += 1
        print(c)


#  Exercise5: append each item with a Dr. prefix to the lst.
def exercise5():
    print("Given a list of name, append each item with a Dr. prefix to the lst.")
    name = ["Phil", "Oz", "Seuss", "Dre"]
    doctors = []
    for i in name:
        doctors.append("Dr." + i)
    print(doctors)


#  Exercise6: append each number with square to the new list
def exercise6():
    print("Given a list of number, append each number with square to the new list")
    numbers = [3, 7, 6, 8, 9, 11, 15, 25]
    squared = []
    for i in numbers:
        squared.append(i ** 2)
    print(squared)


# Exercise7: appends each number to the new list if it's positive.
def exercise7():
    print("Given a list of number, appends each number to the new list if it's positive")
    numbers = [111, 32, -9, -45, -17, 9, 85, -10]
    posNumbers = []
    for i in numbers:
        if i > 0:
            posNumbers.append(i)
        else:
            break
    print(posNumbers)


# Exercise8: append the value minus 1000 for each key to the new list if the value is above 1000.
def exercise8():
    print("Given a dict, you need to append the value minus 1000 for each key to the new list if the value is above "
          "1000")
    dictionary = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
    morethan1k = []
    for i in dictionary:
        value = dictionary[i] - 1000
        if value > 1000:
            morethan1k.append(value)
    print(morethan1k)


#  Exercise9:  appends the type of each element in the first list to the second list
def exercise9():
    print("Given a list of data type, appends the type of each element in the first list to the second list")
    typeList = [3.14, 66, "Teddy Bear", True, [], {}]
    newList = []
    for i in typeList:
        newList.append(type(i))
    print(newList)
