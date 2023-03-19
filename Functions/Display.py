from Exercises import ForLoopExercise, WhileLoopExercise
from Commontexts import forloop, whileloop


def displayForLoopQuesAns(option, question):
    if option.lower() == forloop:
        if question == 1:
            ForLoopExercise.exercise1()
        elif question == 2:
            ForLoopExercise.exercise2()
        elif question == 3:
            ForLoopExercise.exercise3()
        elif question == 4:
            ForLoopExercise.exercise4()
        elif question == 5:
            ForLoopExercise.exercise5()
        elif question == 6:
            ForLoopExercise.exercise6()
        elif question == 7:
            ForLoopExercise.exercise7()
        elif question == 8:
            ForLoopExercise.exercise8()
        elif question == 9:
            ForLoopExercise.exercise9()
    elif option.lower() == whileloop:
        if question == 1:
            WhileLoopExercise.exercise1()
        elif question == 2:
            WhileLoopExercise.exercise2()
        elif question == 3:
            WhileLoopExercise.exercise3()
        elif question == 4:
            WhileLoopExercise.exercise4()