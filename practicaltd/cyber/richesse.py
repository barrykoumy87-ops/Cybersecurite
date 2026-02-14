crrect_password = "admi1234"
tentative = 3
while tentative > 0:
    password = input("Mot de passe:")
    if password == crrect_password:
        print("connexion reussie")
        break
    else:
        tentatives -= 1
        print("mot de passe incorrect")
    if tentatives == 0:
        print("mot de passe bloque")