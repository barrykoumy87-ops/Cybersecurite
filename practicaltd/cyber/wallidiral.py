# Programme de verification de mot de passe
mot_de_passe = input("entrer le mot de passe : ")
if len(mot_de_passe) < 8:
    print("mot de passe court")
elif mot_de_passe.isdigit():
    print("mot de passe faible")
elif mot_de_passe.isalpha():
    print("mot de passe trop faible (que des lettres)")
else:
    print("mot de passe acceptable")