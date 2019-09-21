#Lista Extra
#Gabriel Alvares de Sousa Guimaraes
#119157255

#1:
# a) -5  INT
# b) 5   INT
# c) 1   INT
# d) 1.0  FLOAT
# e) -3.0 FLOAT
# f) 0.0 FLOAT
# g) 1.0 FLOAT
# h) 4.0 FLOAT
# i) 1.3000000000007 FLOAT
# j) 3.0 FLOAT
# k) 1.5 FLOAT
# l) -4.0 FLOAT
# m) 1.0 FLOAT

#2
# a) Valido
# b) Valido
# c) Invalido, não pode iniciar com número
# d) Valido
# e) Invalido, palavra reservada
# f) Invalido, não pode conter caracter especial
# g) Invalido, não pode iniciar com número
# h) Valido
# i) Invalido, não pode conter caracter espcial
# j) Invalido, é uma string, não variavel
# k) Valido

#3
# a) a=10, b=0
# b) a=10, b=2
# c) a=1, b=0.66666
# d) a=63, b=9
# e) a=2, b=0

#4
# a) Incorreto, tipos de dados diferentes
# b) "abcdef"
# c) Incorreto
# d) "abcabcabc"
# e) 'abcabcabcabc9'
# f) "xxyyyxxyyy"
# g) Incorreto, operador - não está definido para strings

#5
# a) 456.0, float
# b) Incorreto, "aaaa" não pode ser convertido para int
# c) 2222.2, float
# d) "111555", str
# e) 33.2001, float
# f) "10.0", str

#6
# a) "9bZ"
# b) ""
# c) "9876543210bcdefZ"
# d) "aXY"
# e) "9876543210abcdefXYZ"
# f) "531"
# g) "5ed"
# f) "02468"

#7
# a) Incorreto, a[0:1] e c[1:] são listas e b[2] é string, não é possível concatená-las
# b) ['maria', 'come', 'come', 'evita']
# c) Incorreto, Só existe 1 item na lista, logo não é possível selecionar o de index 2
# d) ['maria', 'pedro', 'pão']
# e) ['joão', 'maria', 'pedro', 'gosta', 'come', 'evita']
# f)  Incorreto, operador - não está definido para listas
# g) "gosta"
# h) "riaevitabolo"
# i) "aranja"

#8
# a) x=[20,20,30], y=["a", "e", 30, "o", "u"]
# b) x=[10, [20, 30], 30], y=['a', ['i', 'o', 'u'], 'i', 'o', 'u']
# c) x=[20,30], y=30
# d) x=[20,30], y=['a', 'e', 'i', 'o']
# e) x=[['a', 'e', 'i', 'o', 'u'], 20, 30], y=[[10, 20, 30], 'a', 'e', 'i', 'o', 'u']
# f) x=y=[10, 20, 30, 'a', 'e', 'i', 'o', 'u']
# g) x=[10,30], y=['a', 'e', 'o', 'u']

#9
# a= [7, 4]
# b= [1, 4, [7, 4]]
# c= [7, 4]
# d= [1, 4, [7, 4]]

#10
#a=1
#b=2
#c=3

#11
#Funções Auxiliares

def pos(pos,vel,a,t):
    return pos + t*vel + (a*(t*t))/2

def vel(vel,a,t):
    return vel + a*t

#Função principal

def posicao(posi, velo, a, t):
    # Entrada esperada: (pos_x, pos_y, pos_z), (vel_x, vel_y, vel_z), (a_x, a_y, a_z)
    posicao_x = pos(posi[0], velo[0], a[0], t)
    posicao_y = pos(posi[1], velo[1], a[1], t)
    posicao_z = pos(posi[2], velo[2], a[2], t)
    velocidade_x = vel(velo[0], a[0], t)
    velocidade_y = vel(velo[1], a[1], t)
    velocidade_z = vel(velo[2], a[2], t)
    return 'Posição:'+ str((posicao_x,posicao_y,posicao_z)), "Velocidade" + str((velocidade_x,velocidade_y,velocidade_z))


print(posicao((1,1,1),(1,1,1),(1,1,1),1))

#12


def previdencia (sal, op):
    op = op.lower()
    if op=="trabalhador comum":
        if sal<=1751.81:
            return "O valor é R$ {:.2f}".format(sal*8/100)
        elif 1751.82 <= sal <= 2919.72:
            return  "O valor é R$ {:.2f}".format(sal*9/100)
        elif 2919.73 <= sal <= 5839.45:
            return "O valor é R$ {:.2f}".format(sal*11/100)
    elif op=="contribuinte avulso" and 199.60 <= sal <= 1167.89:
        return "O valor é R$ {:.2f}".format(sal/5)


print(previdencia(3000, "trabalhador comum"))

#13


def irpf (sal):
    if sal <= 1903.98:
        return "O valor do imposto é R$ 0"
    elif 1903.99 <= sal <= 2826.65:
        return "O valor do imposto é R$ {:.2f}".format((sal*7.5/100)-142.80)
    elif 2826.66 <= sal <= 3751.05:
        return "O valor do imposto é R$ {:.2f}".format((sal*15/100)-354.80)
    elif 3751.06 <= sal <= 4664.68:
        return "O valor do imposto é R$ {:.2f}".format((sal*22.5/100)-636.13)
    elif sal > 4664.68:
        return "O valor do imposto é R$ {:.2f}".format((sal*27.5/100)-869.36)


print(irpf(2670))

#14


def salario (sal):
    desc_prev = previdencia(sal, "trabalhador comum")
    desc_prev = float(desc_prev[desc_prev.find("$")+2::])
    sal -= desc_prev
    desc_irpf = irpf(sal)
    desc_irpf = float(desc_irpf[desc_irpf.find("$")+2::])
    sal-= desc_irpf
    return sal

print(salario(3000))


#15


def aliquota (sal):
    desc_prev = previdencia(sal, "trabalhador comum")
    desc_prev = float(desc_prev[desc_prev.find("$")+2::])
    sal -= desc_prev
    valor_irpf = irpf(sal)
    valor_irpf = float(valor_irpf[valor_irpf.find("$")+2::])
    return "{:.1f} %".format(valor_irpf/sal)

print(aliquota(3000))
