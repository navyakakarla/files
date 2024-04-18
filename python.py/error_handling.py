#a=1
#print(b)
#if we get error like this
try:
    print(b)
except:
    print("error")
else:
    print("no error")
finally:
    print("always")
#we are giving right way
    try:
        print("b")
    except:
        print("error")
    else:
        print("no error")
    finally:
        print("finally")
#type error
    try:
        print('a'+32)
    except TypeError:
        print("type error")
    except ValueError:
        print("value error")
