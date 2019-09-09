def prob_1(s):
    return len(s.split())

def prob_2(s, palavra, i_1, i_2):
    ind = str.find(s, palavra)
    s = s[:ind] + s[ind + len(palavra)::]
    print(s)








def prob_3(s):
    lista=[]
    for letra in s:
        if letra!= " ":
            lista.append(letra)
        else:
            lista.append("#")
    return "".join(lista)
            

def prob_4(s, char):
    pass


def prob_5(tup):
    tup1=[]
    tup2=[]

    if type(tup[0]) == str:
        tup1.append(tup[0])
    elif type(tup[0]) == int or type(tup[0]) == float or type(tup[0]) == complex:
        tup2.append(tup[0])


    if type(tup[1]) == str:
        tup1.append(tup[1])
    elif type(tup[1]) == int or type(tup[1]) == float or type(tup[1]) == complex:
        tup2.append(tup[1])

    if type(tup[2]) == str:
        tup1.append(tup[2])
    elif type(tup[2]) == int or type(tup[2]) == float or type(tup[2]) == complex:
        tup2.append(tup[2])

    return tuple(tup1), tuple(tup2)




def prob_5_alternativa(tup):
    tup1=[]
    tup2=[]
    for i in range(0,3):
        if type(tup[i]) == str:
            tup1.append(tup[i])
        elif type(tup[i]) == int or type(tup[i]) == float or type(tup[i]) == complex:
            tup2.append(tup[i])     

    return tuple(tup1), tuple(tup2)
    
 
   


def prob_6(l1,l2):
    return [ l1[0], l2[0], l1[1], l2[1], l1[2], l2[2] ]


def prob_6_alternativa(l1,l2):
    lista = []
    for i in range(0,3):
        lista.append(l1[i])
        lista.append(l2[i])
    return lista
        
