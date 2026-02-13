#Partie 2#

def scalar_prod(v,w):
    res = 0
    for i in range(len(v)) :
       res+= v[i]*w[i]                                  # on additionne dans la variable res :  les multiplication des coordonnées de chaque vecteurs
    return res

def scalar_mult(mu,v) :
    return   [v[i]*mu for i in range(len(v))]           # compréhension de liste ou on multiplie chaque coordonnée du vecteur par le scalaire

def proj(v,w) :
    res0 = (scalar_prod(v,w))                           # calcule le produit scalaire
    resfinale= scalar_mult(res0/scalar_prod(v,v),v)
    return resfinale                                    # renvoie la projection orthogonale

def subtract(v,w) :
    return[ v[i]-w[i] for i in range(len(v))]           # compréhension de liste  qui renvoie la différence entre deux vecteurs

def norme(v) :
    res = 0
    for i in v :
        res+=i**2
    return scalar_mult((res**(1/2))**(-1), v)           # renvoie un vecteur de norme 1 dans sa base

def Gram_Schmidt(E) :
    u=[]
    for k in range(len(E)):
        uk= [E[k]]
        for j in range(k):
             uk.append(subtract(uk[j],proj(u[j],E[k])))  # on soustrait le j-ème vecteur avec sa j-eme projection
        u.append(norme(uk[-1]))                          # on normalise chaque vecteur pour avoir une base orthonormée
    return u
