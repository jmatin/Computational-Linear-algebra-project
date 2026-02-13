#Partie 1#

def compose_perm(alpha, beta):
    res=[]                                              # initialise une liste vide qui contiendra le résultat de la permutation
    for i in range(len(alpha)):                         # itère autant de fois qu'il y a d'éléments dans la permutation
        res.append(alpha[beta[i]])                      # augmente la liste du résultat de la composition pour chaque élément
    return res                                          # renvoie la liste finale

def is_id(alpha):
    res=[]                                              # initialise une liste vide qui contiendra le résultat de la permutation
    for i in range(len(alpha)):                         # itère autant de fois qu'il y a d'éléments dans la permutation
        res.append(alpha[alpha[i]])                     # augmente la liste du résultat de la composition pour chaque élément
    if res==alpha:                                      # teste si la liste résultante de la composition équivaut à l'identité et:
        return True                                     # retourne vrai si c'est le cas
    else:
        return False                                    # retourne faux si ce n'est pas le cas

def order1(alpha):
    r=compose_perm(alpha,alpha)                         # calcule la composition de alpha avec elle-même
    n=1                                                 # après cette première composition, n vaut donc 1
    while r!= alpha:                                    # tant que les compositions successives ne renvoient pas la permutation initiale, on fait:
        n+=1                                            # augmentation de n d'une unité à chaque nouvelle alpha-permutation
        r = compose_perm(alpha,r)                       # recomposition
    return n                                            # renvoi du nombre de fois qu'il a fallu recomposer pour obtenir l'identité := l'ordre


def cycle_lengths(alpha):
    res=[]                                              # initialisation d'une liste vide qui contiendra les longueurs de cycles
    cumul=[]                                            # initialisation d'une liste vide dans laquelle on mettra tous les éléments ayant déja été permutés
    for i in alpha:                                     # pour chaque élément d'alpha
        if i not in cumul:                              # si l'élément n'a pas encore été permuté:
            iteration = alpha[i]                        # on lui applique la permutation
            cumul.append(iteration)                     # et on le rajoute dans cumul pour savoir qu'il a maintenant été permuté
            n=1                                         # on augmente n de 1 car 1 élément a été permuté dans ce cycle
            while iteration != i:                       # tant que la permutation n'a pas ramené à l'élément de départ, on continue à:
                iteration = alpha[iteration]            # permuter
                cumul.append(iteration)                 # et rajouter chaque élément déja permuté à la liste cumul
                n+=1                                    # et rajouter une unité à chaque permutation pour connaitre la longueur du cycle
            res.append(n)                               # une fois le cycle bouclé, rajouter sa longueur à la liste
    return res                                          # quand tous les éléments ont été permutés, on renvoie la liste contenant toutes les longueurs de cycles

def Euclid(a,b):                                        # faire l'algorithme d'Euclide sur les 2 nombres a et b
    while b !=0:                                        # tant que le second nombre est différent de 0:
        t=b
        b=a%b                                           # on prend le reste de la division entière de a et b et on l'assigne à b
        a=t                                             # et on remplace a par b pour continuer la procédure
    return a

def lcm_of_list(l):
    ppcm = l[0] * l[1] // Euclid(l[0], l[1])            # on calcule le plus petit commun multiple pour les 2 premières longueurs de cycle
    for nombre in l[2:]:                                # on continue pour les autres longueurs de cycle dans la liste,
        ppcm = ppcm * nombre // Euclid(ppcm, nombre)    # en prenant aussi le ppcm avec celui déjà obtenu au tour d'avant
    return ppcm                                         # on renvoie le plus petit commun multiple final obtenu

def order2(alpha):
    return lcm_of_list(cycle_lengths(alpha))            # d'après le théorème, on prend le plus petit commun multiple
                                                        # des longueurs de cycle et on obtient l'ordre


