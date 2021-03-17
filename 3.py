berbalik = False
orang = 0
numb = 0
while numb < 100 :
    numb  += 1
    #Bilangan nya berbalik atau tidak
    if berbalik == True :
        orang -= 1
    elif berbalik == False:
        orang += 1
    #Urutan ke 7 = berbalik
    if numb % (7) == 0:
        berbalik = not berbalik
    #membuat range
    if orang == 11:
        orang = 1
    elif orang == 0:
        orang = 10
    #skip 1 orang jika numb 11
    if numb % 11 == 0:
        if orang == 10 and berbalik == False:
            orang = 1
        elif orang == 1 and berbalik == True:
            orang = 10
        elif berbalik == True:
            orang -= 1
        elif berbalik == False:
            orang += 1
    print("Orang ke", orang, "mengatakan", numb)
   