

#if condition,else (if true)#
if  True:
    print("nenu if")
else:
    print("nenu else")
#if condition,else(if false)
if False:
    print("i am if")
else:
    print("i am else")
#if condition,elif condition,else condition#
    if False:
        print("i am if")
    elif True:
        print("i am elif")
    else:
        print("i am else")
    #nested if#
    if True:
        print("outer if")
        if True:
            print("inner if") 
        else:
            print("inner else")
    else:
        print("ourter else") 
        
       #nested if#
        if True:
            print("outer if")
            if False:
                print("inner if") 
            else:
                print("inner else")
        else:
            print("ourter else") 

    #age=18#
    age=18
    if age>18:
        print("you can vote")
    elif age==18:
        print("you can vote")
    else:
        print("wait")

    #for multiple condtions we can use logical operators#
    age=18
    if age>18 or age==18:
        print("you can vote")
    else:
        print("wait")


        