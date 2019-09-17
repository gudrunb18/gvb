x,y = 1,1

def north(x,y): 
    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):
        return False
    return True

def east(x,y): 
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        return False
    return True

def west(x,y):
    if y == 1 or x == 1 or (x,y) == (3,2):
        return False
    return True

def south(x,y):
    if y == 1 or (x,y) == (2,3):
        return False
    return True

def string(n,e,s,w):
    direction = ""
    while direction == "":
        if n == True:
            direction += "(N)orth"
        elif e == True:
            direction += "(E)ast"
        elif s == True:
            direction += "(S)outh"
        elif w == True:
            direction += "(W)est"
    if e == True and direction != "(E)ast":
        direction += " or (E)ast"
    if s == True and direction != "(S)outh":
        direction += " or (S)outh"
    if w == True and direction != "(W)est":
        direction += " or (W)est"
    return direction
    
def command_call():
    i = input("Direction: ")
    i = i.upper()
    return i

def translocator(boolean):
    if boolean == True:
        return 1
    return 0

def move(x,y,string):
    if string == "N":
        y += translocator(N)
    elif string == "S":
        y -= translocator(S)
    elif string == "W":
        x -= translocator(W)
    elif string == "E":
        x += translocator(E)
    return x,y
    

while (x,y) != (3,1):
    hnit1 = x
    hnit2 = y
    N,E,S,W = True,True,True,True
    N = north(x,y)
    E = east(x,y)
    S = south(x,y)
    W = west(x,y)
    directions = string(N,E,S,W)
    print("You can travel: " + directions + ".")
    command = ""
    while (x,y) == (hnit1,hnit2):
        command = command_call()
        x,y = move(x,y,command)
        if (x,y) == (hnit1,hnit2):
            print("Not a valid direction!")
print("Victory!")


#hæ
