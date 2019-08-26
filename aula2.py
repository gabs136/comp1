import math 
def pi():
    return 3.14159265359

#########################################################
def prob_1_a_media_2n(x,y):
    return (x+y)/2


def prob_1_a(x,y,z,w):
    #Média entre 4 números
    #float, float -> float
    return (media_2n(x,y)+ media_2n(z,w))/2

def prob_1_b(din, val):
    #Maior número de bombons
    #float,float -> int
    return (din//val), din-((din//val)*val)


##########################################################
def prob_2_a(a,b):
    #Hipotenusa dado os catetos
    #float,float -> float
    return math.sqrt(a**2 + b**2)

def prob_2_b(x_1,y_1,x_2,y_2):
    #Distância entre dois pontos
    #float, float -> float
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

def prob_2_c(a,b):
    #Perímetro de um triângulo retângulo
    #float, float -> float
    return prob_2_a(a,b) + a + b

def prob_2_d(ang):
    #Soma do quadrado do seno e quadado do cosseno de um ângulo
    #float, float -> float
    return (math.sin(ang)**2) + (math.cos(ang)**2)
############################################################

def prob_3(raio):
    #Comprimento do círculo
    #float -> float
    return 2*pi()*raio

def prob_4(raio, dist):
    #Número de voltas
    #float -> float
    return dist/prob_3(raio)
############################################################
def prob_5_discriminante(a,b,c):
    return b**2 -4*a*c

def prob_5(a,b,c):
    #Raízes da equação de parâmetros a,b e c
    #float, float, float -> float
    delta = math.sqrt(prob_5_discriminante(a,b,c))
    r_1 = ((b*-1)+ delta)/(2*a)
    r_2 = ((b*-1)- delta)/(2*a)
    return delta, r_1, r_2
############################################################        
def prob_6(raio, ang=360):
    #Área do setor circular
    #float, float -> float
    return (ang/360)*pi()*(raio**2)

############################################################
def prob_7_a(a_1, a_n, r):
    return ((a_n - a_1)/r) + 1

def prob_7_b(a_1, a_n, n):
    return ((a_1 + a_n)*n)/2
#############################################################
def prob_8(a,b,c):
    #Quantidade máxima de bolos
    #int, int, int -> int
    possivel_farinha = a//2
    possivel_ovos = b//3
    possivel_leite = c//5

    if possivel_farinha < possivel_ovos and possivel_farinha < possivel_leite:
        result = possivel_farinha
    elif possivel_ovos < possivel_farinha and possivel_ovos < possivel_leite:
        result = possivel_ovos
    else:
        result = possivel_leite

    return result
    
    
