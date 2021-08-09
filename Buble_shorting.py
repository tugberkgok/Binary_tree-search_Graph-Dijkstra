def buble(listee):
    i =0
    j=1
    t = 0
    #print(listee)
    #liste = list
    while j < len(listee):
        #print(liste)
        #print(len(liste))
        #print("i: {} \nj: {}".format(i,j))
        #print(listee)
        if listee[i] > listee[j]:
            a=listee[j]
            listee[j] = listee[i]
            listee[i] = a
            i = i+1
            j = j+1
        elif listee[i] < listee[j]:
            i = i+1
            j = j+1
        elif listee[i] == listee[j]:
            i = i+1
            j = j+1
        t = t+1
    print(listee)
    return listee

def selection_short(short):
    for i in range(len(short)):
        lowest_value_index = i
        for j in range(i+1,len(short)):
            if short[j] < short[lowest_value_index]:
                lowest_value_index = j
        short[i], short[lowest_value_index] = short[lowest_value_index], short[i]

    print(short)

newlist=[]
Listee= [5,2,7,3,12,4566,231,23,78,43]
#buble(Listee)
s = selection_short(Listee)
