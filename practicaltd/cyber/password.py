# Ce script permet de tester si un mot de pass est securise ou pas

# Tester si un mot de passe respecte les regles de securite

def teste_pass():
   password = input("please enter your password:")
   if len(password) < 8:
      print("Ce mot de passe est facil par ce qu'il a moins de 8 caracteres.")
      return
   elif not any(c.isalpha() for c in password):
      print("Ce mot de passe n'est pas securise, il doit contenir des chiffres.")
      return
   elif not any(c.isdigit() for c in password):
      print("Ce mot de passe n'est pas securise, il doit contenir des lettres et des symboles.")
      return
   elif not any(not c.isalnum()for c in password):
      print("Ce mot de passe n'est pas securise, il doit contenir des caracteres")
   else:
      print("le mot de passe est securise")

teste_pass()


        
