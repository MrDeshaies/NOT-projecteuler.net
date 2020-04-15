liste = ["aaaa", "", "zzzzzz", "bzoznzjzozuzr"]
def valeur(mot):
    return sum([ord(lettre)-ord('A')+1 for lettre in mot.upper()])
mot = max(liste, key=valeur)
print(mot, valeur(mot))