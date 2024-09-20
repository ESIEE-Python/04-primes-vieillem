'''On importe la fonction sqrt du module math pour vérifier si le nombre cherché est premier'''
from math import sqrt

#### Fonction secondaire


def isprime(p):
    '''Prends en entrée un nombre entier p, et retourne si oui ou non c'est un nombre entier
    L'utilisateur va donc choisir un nombre p que l'on va tester dans cette fonction'''
    pr = True  #On donne de base que le nombre est premier
    dp = round(sqrt(p)) + 1
    for i in range(2, dp):
        g = p % i
        if g == 0:
            pr = False # On met que le nombre n'est pas premier car ne respecte pas les conditions
    if p == 1:
        pr = False # 1 n'est pas un nombre premier
    return pr #On retourne le résultat

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
