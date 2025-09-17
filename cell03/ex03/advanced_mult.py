#cell 3-3
i = 0
while i < 11 :
    print(f'Table de {i}: ',end="")
    j = 0
    k = i
    while j <10 :
        print(k,end=" ")
        k += i
        j += 1
    print(" ")
    i += 1