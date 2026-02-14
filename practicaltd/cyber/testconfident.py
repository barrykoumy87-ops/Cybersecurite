# Je suis entrain de faire un script de programme pour bloquer un mot de passe apres 3 tentatives.
# Dans ce cas on a besoin de deux variables qui sont le nom d'utilisateur et le mot de passe.
# La valeur maximale est de 3 essais.
# Le programme doit contenir une fonction qui permetra a l'utilisateur de faire ces 3 essais et s'il depasse 
# ces 3 essais le programme le bloque.

max = 3

def tentatives_essai():
    correct_user_name = "koumybarr"
    correct_password = "mamou124@"
    attempts = 0
    
    while attempts < max:
        username = input("entrer username:")
        password = input("entrer password:")

        if username == correct_user_name and password == correct_password:
            print("votre mot de passe est  correct")
            return
        else:
            attempts += 1
            print("mot de passe ou nom d'utilisateur incorrect")
        
    print("desole vous avez essaye plus de 3 fois, compte bloque")

print("secure login system")
tentatives_essai()
