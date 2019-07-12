def getDate():
    import datetime
    return datetime.datetime.now()


#==============Reading Part =========================

#--------------- Mayur Reading function -----------------
def rMayur():
    ''' This function used for only Reading Information of Mayur'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        f = open("MayurExe.txt")
        print(f.read())
        f.close()
    elif (cho == "D" or cho == "d"):
        f = open("MayurDit.txt")
        print(f.read())
        f.close()
    else:
        print("Input is invaild")


#--------------- Jaydip Reading function -----------------
def rJaydip():
    ''' This function used for only Reading Information of Jaydip'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        f = open("JaydipExe.txt")
        print(f.read())
        f.close()
    elif (cho == "D" or cho == "d"):
        f = open("JaydipDit.txt")
        print(f.read())
        f.close()
    else:
        print("Input is invaild")

#--------------- Vishal Reading function -----------------
def rVishal():
    ''' This function used for only Reading Information of Vishal'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        f = open("VishalExe.txt")
        print(f.read())
        f.close()
    elif (cho == "D" or cho == "d"):
        f = open("VishalDit.txt")
        print(f.read())
        f.close()
    else:
        print("Input is invaild")





#--------------- Main Reading function -----------------
def readInfo():
    '''This function used for only Reading Information '''
    print("\n Select the number which person information you want to RETRIVE:\n 1.Mayur \n 2.Jaydip \n 3.Vishal" )
    print("What's your choise:\t")
    val = int(input())
    if (val == 1):
        print("Opening Mayur File")
        rMayur()
    elif (val == 2):
        print("Opening Jaydip File")
        rJaydip()
    elif (val == 3):
        print("Opening Vishal File")
        rVishal()
    else:
        print("Input is invaild")


#==============Writing Part =========================

#--------------- Mayur Writing function -----------------
def wMayur():
    ''' This function used for only Writing Information of Mayur'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        print("What you want to Input:\t")
        info = input()
        f = open("MayurExe.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()

    elif (cho == "D" or cho == "d"):
        print("What you want to Input:\t")
        info = input()
        f = open("MayurDit.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()
    else:
        print("Input is invaild")


#--------------- Jaydip Writing function -----------------
def wJaydip():
    ''' This function used for only Writing Information of Jaydip'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        print("What you want to Input:\t")
        info = input()
        f = open("JaydipExe.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()
    elif (cho == "D" or cho == "d"):
        print("What you want to Input:\t")
        info = input()
        f = open("JaydipDit.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()
    else:
        print("Input is invaild")

#--------------- Vishal Writing function -----------------
def wVishal():
    ''' This function used for only Writing Information of Vishal'''
    print("What you want to read\nE = Exercise \nD = Dite")
    cho = input()
    if (cho == "E" or cho == "e"):
        print("What you want to Input:\t")
        info = input()
        f = open("VishalExe.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()
    elif (cho == "D" or cho == "d"):
        print("What you want to Input:\t")
        info = input()
        f = open("VishalDit.txt","a")
        time = str(getDate())
        f.write(time+": "+info+"\n")
        f.close()
    else:
        print("Input is invaild")


#--------------- Main Inserting function -----------------
def insertInfo():
    '''This function used for Writing Information'''
    print("\n Select the number which person information you want to RETRIVE:\n 1.Mayur \n 2.Jaydip \n 3.Vishal" )
    print("What's your choise:\t")
    val = int(input())
    if (val == 1):
        print("Opening Mayur File")
        wMayur()
    elif (val == 2):
        print("Opening Jaydip File")
        wJaydip()
    elif (val == 3):
        print("Opening Vishal File")
        wVishal()
    else:
        print("Input is invaild")





#----------------Start point-----------------------

while(True):
    chk = input("Do you Want to Continue - 1 for Yes or No for any other key:-\t")
    if (chk == "1"):
        print("What you want do \nR = Reading \t I = Insert ")
        choise = input()

        if (choise == "R" or choise == "r"):
            readInfo()
            print("Thank You")
        elif (choise == "I" or choise == "i"):
            insertInfo()
            print("Done")
        else:
            print("Input is invaild")
    else:
        print("Thank You !!!")
        break



