user_corretto = "python"
pass_corretta = "corso2024"
while True:
 username = input("Inserire username: ")
 password = input("Inserire password: ")
 if username == user_corretto and password == pass_corretta:
     print("Benvenuto! Login riuscito.")
     break
 elif username != user_corretto and password != pass_corretta:
      print("Login FALLITO! User e password ERRATI")
 elif username != user_corretto:
      print("Login FALLITO! Nome uttente errato.")
 else:
      print("Login FALLITO! Password non valide.")
      print("Riprova \n")