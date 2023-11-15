#https://replit.com/join/vtrxjnyipv-sol-veronicaver
intento = 0
password = 0
Caracter=0 
p =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q’','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R' ,'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while len(password) <= 8:
  print("Introcuzca un caracter")
  intento += 1 
  Caracter = input(f"{intento}) Ingresa el caracter de tu contraseña: ") 
  password += Caracter

if all(Caracter in p for Caracter in password):
  print("Correcto")
  print(f"Tu contraseña {password} es valida")
else:
  print("Intenta de nuevo")
  print(f"Tu contraseña {password} es invalida")
