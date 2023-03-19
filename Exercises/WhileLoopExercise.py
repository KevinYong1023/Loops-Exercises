def exercise1():
    print("Adds all the numbers up to 100 (inclusive).")
    counter = 0
    total = 0
    while counter <= 100:
        total = total + counter
        counter += 1
        print(total)


def exercise2():
    print("Iterate through the given list and if there is a 100, assign a notification message to the variable "
          "my_message with the index of 100.")
    my_msg = ""
    number = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
    i = 0
    while i < len(number):
        if number[i] == 100:
            my_msg = "There is a 100 at index no:", str(i)
        i += 1

    print(my_msg)


def exercise3():
    print("Appends all the elements in a list to a new list unless the element is an empty string")
    names = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
    newlist = []
    i = 0
    while i < len(names):
        if names[i] != "":
            newlist.append(names[i])
        i += 1
    print(newlist)


def exercise4():
    print("Appends all the elements in a list to a new list and stop append if the element has an empty string")
    names = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
    newlist = []
    i = 0
    while i < len(names):
        if names[i] != "":
            newlist.append(names[i])
        else:
            break
        i += 1
    print(newlist)
