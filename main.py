reverse = False
orang = 0
numb = 0
while numb < 100 :
    numb  += 1
    if reverse == True :
        orang -= 1
    elif reverse == False:
        orang += 1
    if numb % (7) == 0:
        reverse = not reverse
    if orang == 11:
        orang = 1
    elif orang == 0:
        orang = 10
    if numb % 11 == 0:
        if orang == 10 and reverse == False:
            orang = 1
        elif orang == 1 and reverse == True:
            orang = 10
        elif reverse == True:
            orang -= 1
        elif reverse == False:
            orang += 1
    print("Orang ke", orang, "mengambil", numb)
   