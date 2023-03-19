from Functions import Display
from Commontexts import introTitle, introSubtext, choosetext, forloop, whileloop,chosentext,enterquestionnumbertext,thankstext,validtext

print(introTitle)
print(introSubtext)


def chooseLoop():
    while True:
        option = str(input(choosetext))
        if option.lower() == forloop or option.lower() == whileloop:
            print(f"{chosentext} {option.upper()}")
            while True:
                question = int(input(enterquestionnumbertext))
                if question > 0:
                    print(f"{chosentext} {question}")
                    Display.displayForLoopQuesAns(option, question)
                    break
                elif question == 0:
                    break
            break
        elif option.lower() == 'end':
            print(thankstext)
            break
        else:
            print(validtext)


chooseLoop()
