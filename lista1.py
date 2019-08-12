##LISTA 1##

def prob_1(x,y):
    return (x*y)

def prob_2(r_1, r_2):
    return 3.14*((r_1)**2 - (r_2)**2)

def prob_3(x,y):
    return x/y, x%y

def prob_4(a,b,c,x):
    return a*x*x + b*x + c

def prob_5(total):
    return total/10

def prob_6(x,y):
    return (x+y)/2

def prob_7(x,y,p_1,p_2):
    return ((x*p_1)+(y*p_2))/(p_1 + p_2)

def prob_8(vel_cor, larg, vel_barco):
    return (larg/vel_barco)*vel_cor

def prob_9(inicial, n_meses, taxa):
    return(inicial*(1+taxa))

def prob_10(n,q):
    return (1/1-q) - (((q**n) -1)/q-1)

def prob_11(h_1,m_1,s_1,h_2,m_2,s_2):
    return (h_2 - h_1), (m_2-m_1), (s_2-s_1)


def prob_12(total, n_pessoas):
    return (total/10)/n_pessoas

def prob_13(aresta):
    return aresta**3
    
