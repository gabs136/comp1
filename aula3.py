import math 

def prob_1(num):
    #Módulo de um número
    #float -> float
    if num >= 0:
        return num
    else:
        return (-1*num)


def prob_2(a,b,c):
    #Raízes da equação de segundo grau
    #float,float,float ->float
    delta = (b**2 -4*a*c)

    if delta < 0:
        return "Não possui raízes reais"

    elif delta == 0:
        return  ((b*-1)+ math.sqrt(delta))/(2*a)

    else:
        return ((b*-1)+ math.sqrt(delta))/(2*a), ((b*-1)- math.sqrt(delta))/(2*a)
        

def prob_3(x):
    #Triplicar string
    #string -> string
    return 3*x


def prob_4(x):
    #Modelagem da função
    #int -> int

    if x<=2:
        return x

    elif x>2 and x<=3.5:
        return 2

    elif x>3.5 and x<=5:
        return 3

    else:
        return x**2 -10*x +28



def prob_5(x,y):
    if x<y:
        return "O máximo é " + str(y) + " o mínimo é " + str(x)
    elif x>y:
        return "O máximo é " + str(x) + " o mínimo é " + str(y)
    else:
        return "Não existe máximo e mínimo"


def prob_6(idade, tem_carteira):
    #Direito a meia entrada
    #int,bool -> bool

    if idade >= 65 or idade<=21 or tem_carteira == true:
        return True
    else:
        False


def prob_7(c_v, c_e, c_s, f_v, f_e, f_s):
    #Detemrinar o melhor colocado no campeonato
    #int,int,int,int,int,int -> string
    pontos_c = c_v * 3 + c_e*1
    pontos_f = f_v*3 + f_e *1

    if pontos_c == pontos_f and c_s==f_s:
        return "Empate"
    elif pontos_c > pontos_f:
        return "Cormengo"
    else:
        return "Flaminthians"

def prob_8(comps, quant_papel, num_folhas):
    #Determinar se a quantidade de folhas e suficiente
    #int, int ,int -> string

    if quant_papel >= num_folhas * comps :
        return "Suficiente"
    else:
        return "Insuficiente"
    



    
